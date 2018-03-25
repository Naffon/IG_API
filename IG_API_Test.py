import requests
import json
from pprint import pprint

URL = "https://demo-api.ig.com/gateway/deal/session"
API_KEY = "XXXXX"
USER = "XXX"
PASSWORD = "XXXX"
CST = None
X_SECURITY_TOKEN = None

data = {
    "identifier": USER,
    "password": PASSWORD
}

headers = {
    "X-Ig-Api-Key": API_KEY,
    "Content-Type": "application/json; charset=UTF-8",
    "Accept": "application/json; charset=UTF-8"
}

response = requests.post(URL, data=json.dumps(data), headers=headers)

print(response)

CST = response.headers['CST']
X_SECURITY_TOKEN = response.headers['X-SECURITY-TOKEN']
