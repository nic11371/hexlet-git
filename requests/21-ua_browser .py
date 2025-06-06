import requests
import json
import random
from fake_useragent import UserAgent


browser_os_combinations = [
    {"browser": ["Chrome"], "os": "Windows"},
    {"browser": ["Chrome"], "os": "Mac OS X"},
    {"browser": ["Chrome"], "os": "Linux"},
    {"browser": ["Chrome"], "os": "Android"},
    {"browser": ["Firefox"], "os": "Windows"},
    {"browser": ["Firefox"], "os": "Mac OS X"},
    {"browser": ["Firefox"], "os": "Linux"},
    {"browser": ["Firefox"], "os": "Android"},
    {"browser": ["Safari"], "os": "Mac OS X"},
    {"browser": ["Edge"], "os": "Windows"},
    {"browser": ["Opera"], "os": "Windows"},
    {"browser": ["Opera"], "os": "Mac OS X"},
    {"browser": ["Opera"], "os": "Linux"},
    {"browser": ["Opera"], "os": "Android"},
    {"browser": ["Mobile Safari"], "os": "iOS"},
    {"browser": ["Opera"], "os": "iOS"},
    {"browser": ["Chrome"], "os": "iOS"},
]
url = "http://31.130.149.237/right_combination/check"
password = []
for combination in browser_os_combinations:
    ua = UserAgent(os=combination.get('os'), browsers=combination.get('browser')[0])
    headers = {
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        number = data.get('part_of_password')
        password.append(number)

print(sum(password))
