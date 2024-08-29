import requests
from datetime import datetime
import os
os.environ["APP_ID"] = ""
os.environ["API_KEY"] = ""
os.environ["AUTHORIZATION"] = ""
APP_ID = os.environ["APP_ID"]
API_KEY =os.environ["API_KEY"]
AUTH = os.environ["AUTHORIZATION"]
USERNAME = "jomoyeni"
PROJECT = "Joy's copy of My Workouts"
SHEET = "workouts"
sheetyendpoint = "https://api.sheety.co/cb20e1f62f47ac07298f5a8f09de99e7/joy'sCopyOfMyWorkouts/workouts"
exercisendpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
user_input = input("Tell me which exercise you did:")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": AUTH
}

params = {
    "query": user_input
}
today_day = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")
response = requests.post(url=exercisendpoint, json=params, headers=headers)
tot_exer = response.json()
for exer in tot_exer["exercises"]:
    sheet_input = {
        "workout":{
            "date": today_day,
            "time": now_time,
            "exercise": exer["name"].title(),
            "duration": exer["duration_min"],
            "calories": exer["nf_calories"]
        }
    }
    print(sheet_input)
    sheet_response = requests.post(url=sheetyendpoint, json=sheet_input)
print(sheet_response.json())