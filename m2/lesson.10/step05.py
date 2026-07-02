import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import openpyxl
from pprint import pprint
import csv
import time


if __name__ == '__main__':
    books = []
    for i in range(2, 50):

        url = f'https://books.toscrape.com/catalogue/page-{i}.html'
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print('Всё хорошо')
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            all_book = soup.select('article.product_pod')


            for book in all_book:
                link_element = book.select_one('h3 a')
                title = link_element.get('title')
                relative_url = link_element.get('href')
                book_url = urljoin(url, relative_url)

                price_element = book.select_one('p.price_color')
                price = price_element.text.strip()

                rating_element = book.select_one('p.star-rating')
                rating = rating_element.get("class")[1]

                book_data = {
                    "title": title,
                    "price": float(price[2:]),
                    "rating": rating,
                    "url": book_url,
                }
                pprint(book_data)
                print()
                books.append(book_data)

                time.sleep(5)
        else:
            print('Страница не загружается')
            print(response.status_code)


        # field_names = ['title', 'price', 'rating', 'url']
        # with open('books.csv', 'w', newline='', encoding='utf-8') as csv_file:
        #     writer = csv.DictWriter(csv_file, fieldnames=field_names)
        #     writer.writeheader()
        #     writer.writerows(books)
        #     # print("Файл открыт для записи")

    df = pd.DataFrame(books)
    print(df)

    df.to_excel(
        'books.xlsx',
        index=False, )
