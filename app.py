import os
from dotenv import load_dotenv 

load_dotenv() 
import streamlit as st
import pandas as pd
from fetch_live_data import get_weather 
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

# ------------------ Load Grounds Data ------------------
@st.cache_data
def load_ground_data(): 
    df = pd.read_excel("grounds_data.xlsx")
    return df

grounds_df = load_ground_data()

# ------------------ Tool Initialization ------------------
search_tool = SerperDevTool()

# ------------------ Initialize CrewAI Agent ------------------
agent = Agent(
    role="Pitch Analysis Specialist", 
    goal="Analyze pitch and weather data to provide a toss recommendation.",
    backstory="An expert cricket analyst who uses data to predict match conditions.", 
    llm="gemini/gemini-2.5-flash", 
    tools=[search_tool],
    verbose=True, 
    allow_delegation=False
)

# ------------------ Streamlit App UI ------------------
st.title("🏏 AI-based Toss Decision Helper")

team1 = st.text_input("Enter Team 1 Name (e.g., MI)")
team2 = st.text_input("Enter Team 2 Name (e.g., CSK)")

venue_list = grounds_df['stadium'].unique()
selected_venue = st.selectbox("Select the Venue:", venue_list)

if st.button("Get Toss Recommendation"):
    if not team1 or not team2:
        st.warning("Please enter both team names.")
    elif not selected_venue:
        st.warning("Please select a venue.")
    else:
        # This line requires your .xlsx file to be filled out
        match_info = grounds_df[grounds_df['stadium'] == selected_venue].iloc[0]
        
        venue = match_info['stadium']
        pitch_type = match_info['pitch_type']
        
        # This line requires the 'city' column to be filled
        if 'city' not in match_info or pd.isna(match_info['city']):
            st.error(f"Error: The 'city' column in your Excel file is empty for {venue}.")
            st.stop()
            
        city = match_info['city'] 

        st.write(f"🏟 Venue: {venue}")
        st.write(f"📊 Pitch Type: {pitch_type}")
        st.write(f"📊 Match Type: T20")

        # ------------------ Weather ------------------
        st.write(f"🌐 Fetching weather for: {city}")
        weather = get_weather(city)
        if weather[0] is not None:
            temp, humidity, desc = weather
            st.write(f"🌦 Weather: {desc}, {temp}°C, Humidity: {humidity}%")
        else:
            st.warning("⚠️ Could not fetch weather data. Check city or API key.")

        # ------------------ Toss Recommendation ------------------
        query = (
            f"Analyze pitch data for {venue} (a {pitch_type} pitch) "
            f"and current weather ({weather[2]}, {weather[1]}°C, {weather[0]}% humidity) "
            f"for a T20 match between {team1} and {team2}. "
            f"Recommend whether to bat or bowl first and provide a brief reason."
        )

        toss_task = Task(
            description=query,
            expected_output="A clear recommendation to 'bat' or 'bowl' first, with a 1-2 sentence justification.",
            agent=agent
        )

        toss_crew = Crew(
            agents=[agent],
            tasks=[toss_task],
            
            verbose=True 
        )
        
        try:
            st.write("🤖 Getting recommendation from the AI agent...")
            recommendation = toss_crew.kickoff()
            st.success(f"💡 Toss Recommendation: {recommendation}")
        except Exception as e:
            st.error(f"❌ Could not get recommendation: {e}")