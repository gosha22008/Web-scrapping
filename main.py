import requests
from bs4 import BeautifulSoup
import re

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()

url = 'https://habr.com'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

text = response.text

soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    title = article.find('a', class_="tm-article-snippet__title-link")
    href = url + title.attrs.get('href')
    dat = article.find('time')

    request = requests.get(href)
    request.raise_for_status()

    my_text = request.text
    soup = BeautifulSoup(my_text, features='html.parser')
    articles = soup.find_all('article')

    for article in articles:
        for word in KEYWORDS:
            pattern = f'\s?{word}\s?'
            res = re.search(pattern, article.text, re.IGNORECASE)
            if res:
                print('<', dat.text, '>')
                print('<', title.text, '>')
                print('<', href, '> ')
                print('~'*70)