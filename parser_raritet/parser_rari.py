import requests
from bs4 import BeautifulSoup as BS

URL = 'http://price.books.kg/'

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

def get_html(url, params = ''):
    request = requests.get(url, headers = HEADERS, params = params)
    return request

def get_data(html):
    bs = BS(html, features = 'html.parser')
    items = bs.find_all('div', class_ = 'table table-bordered table-striped table-hover')
    raritet_list = []
    for item in items:
        title = item.find('th').get_text()
        href = item.find('a').get('href')
        raritet_list.append({
            'title': title,
             'href': href}
        )
        return raritet_list

def parsing():
    response = get_html(URL)
    if response.status_code == 200:
        raritet_list2 = []
        for page in range(1,2):
            response = get_html("http://price.books.kg/welcome/index/2", params = {'page': page})
            raritet_list2.extend(get_data(response.text))
            return raritet_list2
        else:
            raise Exception('error in parsing')


# print(parsing())
