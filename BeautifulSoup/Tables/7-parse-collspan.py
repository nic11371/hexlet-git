from bs4 import BeautifulSoup
import requests


url = 'https://parsinger.ru/table/8/index.html'
response = requests.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
tags_colspan = soup.find_all(attrs={'colspan': True})
total = [int(c.text) for c in tags_colspan[1:]]

print(sum(total))
