API_KEY = "484a4353d32a2291f4a61d55c447e920"
long = 3.503440
lat = 6.621070
import requests
from twilio.rest import Client

TWILLIOCODE = "62XM55PYRR3K2V1WPBN48UBD"
accountid = "AC867515e1a06ed821ea040195cd3a6e3c"
accttoken = "f78f02c72c0c85c5dee93615202b11a7"
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&cnt={4}&appid={API_KEY}")
data = response.json()
print(data)
print(response)
listt = data["list"]
weather_code = []
will_rain = False
for dict in listt:
    id = dict["weather"][0]["id"]
    weather_code.append(id)
for code in weather_code:
    if code < 800:
        will_rain = True
if will_rain:
    client = Client(accountid, accttoken)
    message = client.messages \
        .create(
        body="It is going to rain today. Remember to bring an umbrella.", from_="+13016850615", to="+2347089940298"
    )
