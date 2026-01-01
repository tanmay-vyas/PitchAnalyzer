grounds = {
    "Wankhede": {"chasing_win_pct": 65, "avg_first_innings": 175, "dew_heavy": True},
    "Chepauk": {"chasing_win_pct": 45, "avg_first_innings": 160, "dew_heavy": False},
    "Eden Gardens": {"chasing_win_pct": 55, "avg_first_innings": 170, "dew_heavy": False}
}

def decide_toss_action(ground, humidity, time_of_day):
    data = grounds.get(ground)
    if not data:
        return "No Data", "Ground data not found."

    dew_factor = "high" if data["dew_heavy"] or humidity > 70 else "low"

    if dew_factor == "high" and time_of_day.lower() == "night":
        return "Bowl First", "Heavy dew likely to make chasing easier."
    elif data["chasing_win_pct"] > 55:
        return "Bowl First", "Historically better for chasing."
    else:
        return "Bat First", "Pitch tends to slow down later."
