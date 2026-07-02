import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
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

        all_book = soup.select('article.product_pod')
        first_book = all_book[0]
        link_element = first_book.select_one('h3 a')
        title = link_element.get('title')
        # title = link_element['title']
        relative_url = link_element.get('href')
        # book_url = url + relative_url
        book_url = urljoin(url, relative_url)

        price_element = first_book.select_one('p.price_color')
        price = price_element.text.strip()

        rating_element = first_book.select_one('p.star-rating')
        rating = rating_element.get("class")[1]

        # print(link_element)
        # print(title)
        # print(book_url)
        # print(price)
        # print(rating)
        # print(type(book_url))

        book_data = {
            "title": title,
            "price": price,
            "rating": rating,
            "url": book_url,
        }
        pprint(book_data)
    else:
        print('Страница не загружается')
        print(response.status_code)



        # {
        #     "title": "Tipping the Velvet",
        #     "price": "£53.74",
        #     "rating": "One",
        #     "url": "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
        # }