from selenium import webdriver
from selenium.webdriver.common.by import By  #By.CSS_SELECTOR  By.XPATH
import time
from pprint import pprint

url = 'https://quotes.toscrape.com/'
driver = webdriver.Chrome()
driver.set_window_position(3500, 0)

try:
    driver.get(url)
    all_quote_card = driver.find_elements(By.CSS_SELECTOR, '.quote')
    quotes = []
    # print(len(all_quote_card))
    # print(type(all_quote_card))
    for quote_card in all_quote_card:
        first_quote = quote_card.find_element(By.CSS_SELECTOR, '.text')
        first_author = quote_card.find_element(By.CSS_SELECTOR, '.author')
        # print(first_quote.text)
        quote_text = first_quote.text
        # print(first_author.text)
        quote_author = first_author.text

        author_link = quote_card.find_element(By.CSS_SELECTOR, 'span a')
        author_url = author_link.get_attribute('href')
        # print(author_url)
        tag_elements = quote_card.find_elements(By.CSS_SELECTOR, '.tags')
        tags = []
        for tag_element in tag_elements:
            tag_text = tag_element.text
            tags.append(tag_text)

        quote_data = {
            "text": quote_text,
            "author": quote_author,
            "author_url": author_url,
            "tags": tags,
        }
        quotes.append(quote_data)
    time.sleep(3)
finally:
    driver.quit()

print('Selenium WebDriver - OK!')
print(len(quotes))
pprint(quotes)

