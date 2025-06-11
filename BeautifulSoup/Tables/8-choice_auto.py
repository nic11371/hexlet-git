from bs4 import BeautifulSoup
import requests
import json


url = 'https://parsinger.ru/table/6/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

table = soup.find('table')
cars = []

headers = [t.text.strip() for t in table.find_all('th')]
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    dictionary = {
        'Марка авто': str(cols[0].text.strip()),
        'Год выпуска': int(cols[1].text.strip()),
        'Тип двигателя': str(cols[4].text.strip()),
        'Стоимость авто': int(cols[7].text.strip())
    }
    cars.append(dictionary)


filtered_cars = [
    car for car in cars
    if (car['Стоимость авто'] <= 4000000 and
        car['Год выпуска'] >= 2005 and
        car['Тип двигателя'] == 'Бензиновый')
]

sorted_cars = sorted(filtered_cars, key=lambda x: x['Стоимость авто'])
result = json.dumps(sorted_cars, indent=4, ensure_ascii=False)
print(result)
