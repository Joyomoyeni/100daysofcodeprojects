STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from twilio.rest import Client

accountid = "AC867515e1a06ed821ea040195cd3a6e3c"
accttoken = "f78f02c72c0c85c5dee93615202b11a7"
ALPHA_API = "H4N444KHTSTVGUVS"
NEWS_API = "82f471cb7d604ea48c47d55f711058f2"
client = Client(accountid, accttoken)

def get_news(percent):
    news_response = requests.get(f"https://newsapi.org/v2/top-headlines?q=tesla&apiKey={NEWS_API}")
    datt = news_response.json()
    headines = []
    if percent > 0:
        tsl = f"TSLA: 🔺{int(percent)}%"
    else:
        tsl = f"TSLA: 🔻{int(percent * -1)}%"
    for n in range(0,2):
        headines.append(datt["articles"][n])
    for new in headines:
        message = client.messages \
            .create(
            body=f"TSLA: {tsl}\nHeadline: {new["title"]}\nBrief: {new["description"]}", from_="+13016850615", to="+2347089940298"
        )


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(
    f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_API}")
data = stock_response.json()
days = []
for key in data["Time Series (Daily)"]:
    days.append(key)
today = float(data["Time Series (Daily)"][days[0]]["4. close"])
yesterday = float(data["Time Series (Daily)"][days[1]]["4. close"])
percent = ((today - yesterday) / yesterday) * 100
print(percent)
if percent < 0:
    if percent < -1:
        get_news(percent)
elif percent > 1:
    get_news(percent)


