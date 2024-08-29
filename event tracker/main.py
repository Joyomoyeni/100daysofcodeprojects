import requests
from datetime import datetime

from dateutil.utils import today

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "jomoyeni"
TOKEEN = "uw8bcj8cb"

user_params ={
    "token": TOKEEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
todday = datetime.today()
graphendpoint = f"{pixela_endpoint}/{USERNAME}/graphs/newgraph/{todday.strftime("%Y%m%d")}"

graph_config = {
    "id": "newgraph",
    "name": "Coding graph",
    "unit": "Km",
    "type": 'int',
    'color': 'shibafu'
}


headers = {
    "X-USER-TOKEN": TOKEEN
}
response = requests.post(url=graphendpoint, json=graph_config, headers=headers)
print(response.text)

postconfig = {
    "id": todday.strftime("%Y%m%d"),
    "name": "Coding graph",
    "unit": "Km",
    "type": 'int',
    'color': 'shibafu',
    "date": "20240828",
    "quantity": "10"
}
response = requests.put(url=graphendpoint, json=postconfig, headers=headers)
print(response.text)