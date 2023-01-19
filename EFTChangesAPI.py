import requests
import json

url = "https://https://api.tarkov-changes.com/v1/ammo"
headers = {
  'Content-Type': 'application/json',
  'AUTH-Token': '3686d0d1139679dda02e'
}

response = requests.get(url, headers=headers)
print(response.text)
