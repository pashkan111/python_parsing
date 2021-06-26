import urllib.request
from product_page import main_json
from main_page import main
import json, io

brands = main()

def make_final():
    a = 1
    final_obj = {}
    for i in brands:
        title = i['title']
        url = i['url']
        objects = main_json(url=f'https://health-diet.ru{url}')
        final_obj[title] = objects
        a += 1
        print(a)
    return final_obj

final_object = make_final()
with io.open('data.json', 'w', encoding='utf-8') as f: 
    f.write(json.dumps(final_object, indent=4, ensure_ascii=False))


    