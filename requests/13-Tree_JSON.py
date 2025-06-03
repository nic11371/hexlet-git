import requests
from collections import Counter

url = 'https://parsinger.ru/3.4/3/dialog.json'

response = requests.get(url, verify=False)

members = [response.json()]

dictionary = {}

def count_members(member):
    for member in members:
        username = member['username']
        print(username)
#         dictionary[username] = Counter(username.values())
# print(dictionary)