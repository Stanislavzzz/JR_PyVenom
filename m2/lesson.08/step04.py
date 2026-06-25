import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from pprint import pprint


# print("Всё работает")
if __name__ == '__main__':
    url = 'https://books.toscrape.com/'
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        print('Всё хорошо')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # first_h3 = soup.find('h3')
        # print(first_h3)
        # print(type(first_h3))

        # all_h3 = soup.find_all('h3')
        # pprint(all_h3)
        # print(len(all_h3))
        # print(type(all_h3))

        # all_books = soup.find_all('article', class_='product_pod')
        # pprint(all_books)
        # print(len(all_books))
        # print(type(all_books))


        # first_book_link = soup.select_one('article.product_pod h3 a')
        # # first_book_link = soup.select_one('article.product_pod')
        # print(first_book_link)
        # print(type(first_book_link))

        # all_book_link = soup.select('article.product_pod h3 a')
        # # first_book_link = soup.select_one('article.product_pod')
        # pprint(all_book_link)
        # print(type(all_book_link))

        # all_book_link = soup.select('article.product_pod')
        first_book_link = soup.select_one('article.product_pod')
        # print(first_book_link)
        link = first_book_link.select_one("h3 a")
        print(link)

    else:
        print('Страница не загружается')
        print(response.status_code)