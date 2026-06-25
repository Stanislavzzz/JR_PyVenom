import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


# print("Всё работает")
if __name__ == '__main__':
    url = 'https://books.toscrape.com/'
    # url = "https://books.toscrape.com/not-found-page/"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print('Всё хорошо')
        html = response.text
        print(len(html))
        print(html[:500])
        # print(response.headers)
        # print(response.url)
        # print(response.content)
    else:
        print('Страница не загружается')
        print(response.status_code)