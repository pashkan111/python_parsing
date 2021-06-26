import requests
from bs4 import BeautifulSoup
import re

URL = 'https://health-diet.ru/base_of_food/food_187936/'
HOST = 'https://health-diet.ru'
HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }

def main_json(url):

    def get_html(url, params=''):
        r = requests.get(url, headers = HEADERS, params=params)
        return r

    html = get_html(url)
    text = html.text
    text = text.encode()

    def parcer():
        soup = BeautifulSoup(text, 'html.parser')
        table = soup.find('table', class_='uk-table mzr-tc-group-table uk-table-hover uk-table-striped uk-table-condensed').find('tbody').find_all('tr')
        products=[]
        for i in table:
            object = {}
            title_el = list(i.find('a').get('title'))[28:]
            title = ''.join(title_el)
            data = []
            kals = i.find_all("td", class_="uk-text-right")
            reg = r"\d[0-9]*[,]?"
            for j in kals:
                data.append(j.text)
            object['title'] = title
            kkals=re.findall(reg, data[0])
            belki=re.findall(reg, data[1])
            zhiri=re.findall(reg, data[2])
            uglevodi=re.findall(reg, data[3])
            object['kals'] = float(kkals[0].replace(',', '.')+kkals[1]) if len(kkals) > 1 else int(kkals[0])
            object['belki'] = float(belki[0].replace(',', '.')+belki[1]) if len(belki) > 1 else int(belki[0])
            object['zhiri'] = float(zhiri[0].replace(',', '.')+zhiri[1]) if len(zhiri) > 1 else int(zhiri[0])
            object['uglevodi'] = float(uglevodi[0].replace(',', '.')+uglevodi[1]) if len(uglevodi) > 1 else int(uglevodi[0])
            products.append(object)
        return products
    return parcer()



        