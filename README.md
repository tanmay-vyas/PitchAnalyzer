PitchAnalyzer ⚡ Agentic AI for Cricket Toss Recommendations

PitchAnalyzer is an agentic AI system that dynamically analyzes cricket match conditions — including pitch type, weather, venue, and match type — and generates context-aware toss recommendations with detailed reasoning.
Unlike static scripts, this AI acts as an autonomous agent, making decisions, adapting to circumstances, and explaining the rationale behind every recommendation. It’s designed for cricket enthusiasts, analysts, and AI/ML portfolio showcases.

🧠 Key Features
🤖 Agentic AI Toss Recommendations
The AI acts autonomously to analyze match conditions.
Provides detailed, human-readable reasoning behind each toss recommendation:
“Toss Recommendation: Bat first. On a sluggish pitch, the surface tends to get slower and offer more to the spinners as the game progresses, making it difficult to chase a target. Setting a score early allows the batting team to take advantage of the best batting conditions.”
Recommendations adapt dynamically to each scenario — pitch, weather, and match type.

🌐 Live Data Integration
Fetches real-time weather and pitch data.
Automatically updates recommendations if conditions change.

📊 Interactive Streamlit Interface
Dropdowns for venue selection.
“Get Toss Recommendation” button triggers the AI agent.
Dynamic status indicators:
Spinner while the AI agent is analyzing
Warning bars if data fetch fails
Green recommendation box for AI output

🧪 Modular & Testable
Python modules for data exploration, fetching, and logic.
Automated tests using pytest for pitch logic and weather handling.

📁 Repository Structure
PitchAnalyzer/
├── .gitignore
├── LICENSE
├── README.md
├── app.py                 # Main Streamlit app
├── explore_data.py        # Data exploration utilities
├── fetch_live_data.py     # Live pitch/venue data fetch
├── fetch_weather.py       # Real-time weather fetch
├── grounds_data.xlsx      # Venue/pitch dataset
├── requirements.txt
├── test_pitch_logic.py
└── test_weather.py

🚀 Getting Started
Prerequisites
Python 3.8+
Virtual environment recommended

python -m venv .venv
.\.venv\Scripts\activate      # Windows
# OR
source .venv/bin/activate     # macOS/Linux

Install Dependencies
pip install -r requirements.txt

Run the App
streamlit run app.py


1. Select a venue/stadium from the dropdown.
2. Click “Get Toss Recommendation”.
3. Watch the AI agent analyze conditions and provide a detailed toss recommendation.

🧾 Example Output
Toss Recommendation: Bat first.
On a sluggish pitch, the surface tends to get slower and offer more to the spinners as the game progresses, making it difficult to chase a target. Setting a score early allows the batting team to take advantage of the best batting conditions.

Output is dynamic and context-aware, changing with every match scenario.

🏷️ Suggested Repo Description & Topics

Description:
Agentic AI-powered cricket toss recommendation system with live weather and pitch integration, interactive Streamlit interface, and adaptive decision-making.

Topics:
python streamlit ai agentic-ai sports-analytics cricket data-visualization

📌 Future Enhancements

Add ML models to predict pitch behavior trends.
Deploy as a web app with cloud backend for real-time tournaments.
Expand AI suggestions to include team strategy recommendations.

🛡️ License

This project uses the MIT License, allowing free use, modification, and redistribution with attribution.
