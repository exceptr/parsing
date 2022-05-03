import requests
import bs4
from heads import HEADERS

url = 'https://habr.com'
KEYWORDS = ['Дизайн', 'Фото', 'Web', 'Python *']

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        if hub in KEYWORDS:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = url + href
            title = article.find('h2').find('span').text
            date_hub = article.find('time').attrs['title']
            result = f'{date_hub} - {title} - {link}'
            print(result)