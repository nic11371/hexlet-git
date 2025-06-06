import requests
import json
import random
from fake_useragent import UserAgent


combinations = {
    "valid_combinations": [
        {
            "browser": "Chrome",
            "os": "Windows",
        },
        {
            "browser": "Chrome",
            "os": "Mac OS X",
        },
        {
            "browser": "Chrome",
            "os": "Linux",
        },
        {
            "browser": "Safari",
            "os": "Mac OS X",
        },
        {
            "browser": "Firefox",
            "os": "Windows",
        },
        {
            "browser": "Firefox",
            "os": "Linux",
        },
        {
            "browser": "Firefox",
            "os": "Mac OS X",
        },
        {
            "browser": "Edge",
            "os": "Windows",
        },
    ],
}
url = "http://31.130.149.237/browser-compatibility/browser-os-check"
password = []
for combination in combinations.get('valid_combinations'):
    ua = UserAgent(os=combination.get('os'), browsers=combination.get('browser'))
    headers = {
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    number = data.get('part_of_password')
    password.append(number)

print(sum(password))
