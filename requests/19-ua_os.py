import requests
import json
import random
from fake_useragent import UserAgent


os_list = ["Mac OS X", "Windows", "Android", "Linux", "iOS"]
url = "http://31.130.149.237/os-challenge/os"
password = []
for os in os_list:
    ua = UserAgent(os=os)
    headers = {
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    number = data.get('part_of_password')
    password.append(number)

print(sum(password))
