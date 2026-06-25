import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


# print("Всё работает")
if __name__ == '__main__':
    url = 'https://books.toscrape.com/'
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print('Всё хорошо')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.prettify())
        # print(soup.head.prettify())
        print('*' * 50)
        print(soup)

    else:
        print('Страница не загружается')
        print(response.status_code)