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
    first_quote_card = driver.find_element(By.CSS_SELECTOR, '.quote')
    # first_quote = driver.find_element(By.CSS_SELECTOR, '.text')
    first_quote = first_quote_card.find_element(By.CSS_SELECTOR, '.text')
    # first_author = driver.find_element(By.CSS_SELECTOR, '.author')
    first_author = first_quote_card.find_element(By.CSS_SELECTOR, '.author')
    print(first_quote.text)
    print(first_author.text)
    # input("Нажмите кнопку...")
    time.sleep(5)
finally:
    driver.quit()

print('Selenium WebDriver - OK!')

# < article class ="product_pod" >
#
# < div class ="image_container" >
#
# < a
# href = "catalogue/a-light-in-the-attic_1000/index.html" > < img
# src = "media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg"
# alt = "A Light in the Attic"
#
#
# class ="thumbnail" > < / a >
#
# < / div >
#
# < p
#
#
# class ="star-rating Three" >
#
# < i
#
#
# class ="icon-star" > < / i >
#
# < i
#
#
# class ="icon-star" > < / i >
#
# < i
#
#
# class ="icon-star" > < / i >
#
# < i
#
#
# class ="icon-star" > < / i >
#
# < i
#
#
# class ="icon-star" > < / i >
#
# < / p >
#
# < h3 > < a
# href = "catalogue/a-light-in-the-attic_1000/index.html"
# title = "A Light in the Attic" > A
# Light in the... < / a > < / h3 >
#
# < div
#
#
# class ="product_price" >
#
# < p
#
#
# class ="price_color" > £51.77 < / p >
#
# < p
#
#
# class ="instock availability" >
#
# < i
#
#
# class ="icon-ok" > < / i >
#
#
# In
# stock
#
# < / p >
#
# < form >
# < button
# type = "submit"
#
#
# class ="btn btn-primary btn-block" data-loading-text="Adding..." > Add to basket < / button >
#
# < / form >
#
# < / div >
#
# < / article >


# body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span.text