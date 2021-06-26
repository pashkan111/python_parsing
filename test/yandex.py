import requests
from bs4 import BeautifulSoup


headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

url = 'https://yandex.ru'
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')

news = soup.find_all('body').

print(f'result: {news}')
