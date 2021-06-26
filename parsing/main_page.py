import requests
from bs4 import BeautifulSoup

URL = 'https://health-diet.ru/base_of_food/food_21545/'
HOST = 'https://health-diet.ru'
HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

def main(url=URL):

    def get_html(url, params=''):
        r = requests.get(url, headers = HEADERS, params=params)
        return r


    html = get_html(url)
    text = html.text
    text = text.encode()


    def parcer():
        soup = BeautifulSoup(text, 'html.parser')
        table = soup.find('table', class_='uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tbody').find_all('tr')

        brands=[]
        for i in table:
            object = {}
            title = i.find('a').text
            url = i.find('a').get('href')
            object['title'] = title
            object['url'] = url
            brands.append(object)

        return brands
    return parcer()




        