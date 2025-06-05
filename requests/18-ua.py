import requests
import json
import random
from fake_useragent import UserAgent

with open('list.json', 'r', encoding='utf-8') as file:
    agent = json.load(file)


url = "http://31.130.149.237/ua_trainer"
ua = UserAgent()
fake = ua.random

statuses = []

for i in agent.get("user_agents"):
    headers = {
        "User-Agent": fake,
    }
    response = requests.get(url, headers=headers, verify=False)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        data = response.json()
        print(data)
