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
        # print(soup)
        # print(type(soup))
        print(soup.h1)
        print(soup.h1.string)
        print(soup.title)
        print(soup.title.string.strip())
        # print(soup.h8)
        print(soup.head.string)
        print(soup.head.text)
        # print(f"Page title: {soup.title.string}")
        # print(soup.h1.prettify())

    else:
        print('Страница не загружается')
        print(response.status_code)