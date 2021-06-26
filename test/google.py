from googleapiclient.discovery import build



class GoogleSearch():
    API_KEY = 'AIzaSyD1Y5kNfTTIdb6TFUrW4TahkV1Yv7wG_sA'
    query = ''

    def __init__(self, query) -> None:
        self.query = query

    def get_info(self, query:str):
        resource = build("customsearch", 'v1', developerKey=self.API_KEY).cse()
        result = resource.list(q=self.query, cx='009557628044748784875:5lejfe73wrw').execute()
        return result

    def get_tags(self):
        res = []
        info = self.get_info(self.query)
        for i in info.get('items'):
            dict = {}
            dict['title'] = i['title']
            dict['link'] = i['link']
            dict['snippet'] = i['snippet']
            res.append(dict)
        return res


search = GoogleSearch('football')
print(search.get_tags())
