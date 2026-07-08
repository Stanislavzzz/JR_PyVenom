from selenium import webdriver
from selenium.webdriver.common.by import By  #By.CSS_SELECTOR  By.XPATH
import time

url = 'https://quotes.toscrape.com/'
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.set_window_position(3500, 0)

try:
    driver.get(url)
    # print(driver.title)
    # all_quote_card = driver.find_elements(By.CSS_SELECTOR, '.quote')
    # all_quote_card = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[1]/div[1]')
    all_quote_card = driver.find_elements(By.XPATH, "//span[@class='text']")

    print(len(all_quote_card))
    print(type(all_quote_card))
    for quote_card in all_quote_card:
        # first_quote = quote_card.find_element(By.CSS_SELECTOR, '.text')
        # first_author = quote_card.find_element(By.CSS_SELECTOR, '.author')
        # print(first_quote.text)
        # print(first_author.text)
        print(quote_card.text)
    time.sleep(5)
finally:
    driver.quit()

print('Selenium WebDriver - OK!')


# /html/body/div/div[2]/div[1]/div[1]/span[1]
# /html/body/div/div[2]/div[1]/div[1]/span[1]/text()