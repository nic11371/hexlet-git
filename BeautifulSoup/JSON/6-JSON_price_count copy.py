import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
dictionary = {}
# {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
for item in response:
    total = int(item['count']) * int(item['price'][:-4])
    if item['categories'] in dictionary:
        dictionary[item['categories']] += total
    else:
        dictionary[item['categories']] = total

print(dictionary)
