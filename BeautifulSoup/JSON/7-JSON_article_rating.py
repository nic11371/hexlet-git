import requests

url = 'https://parsinger.ru/4.6/1/res.json'

response = requests.get(url=url, verify=False).json()
dictionary = {}
# {'watch': N, 'mobile': N, 'mouse': N, 'hdd': N, 'headphones': N}
for item in response:
    total = int(item['article']) * int(item['description']['rating'])
    if item['categories'] in dictionary:
        dictionary[item['categories']] += total
    else:
        dictionary[item['categories']] = total

print(dictionary)
