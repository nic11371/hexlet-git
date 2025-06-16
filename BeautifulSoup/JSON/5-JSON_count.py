import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
dictionary = {}
# {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
for item in response:
    if item['categories'] in dictionary:
        dictionary[item['categories']] += int(item['count'])
    else:
        dictionary[item['categories']] = int(item['count'])

print(dictionary)
