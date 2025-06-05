from bs4 import BeautifulSoup
import requests
import lxml


with open('BeautifulSoup/index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')
    tag_link = soup.link
    print(tag_link.get('href'))