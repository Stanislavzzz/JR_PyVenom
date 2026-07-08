from selenium import webdriver
from selenium.webdriver.common.by import By  #By.CSS_SELECTOR  By.XPATH
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://quotes.toscrape.com/search.aspx'
driver = webdriver.Chrome()
driver.set_window_position(3500, 0)

try:
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    author_select = driver.find_element(By.CSS_SELECTOR, "#author")
    author_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#author")))
    author_select.send_keys('Albert Einstein')

    # time.sleep(1)
    author_select = driver.find_element(By.CSS_SELECTOR, "#tag")
    author_select.send_keys('change')
    # time.sleep(1)
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()

    # all_quote_card = driver.find_element(By.CSS_SELECTOR, '.quote')
    # quotes = []

    # first_quote = all_quote_card.find_element(By.CSS_SELECTOR, '.text')
    # first_author = all_quote_card.find_element(By.CSS_SELECTOR, '.author')

    # time.sleep(3)
finally:
    driver.quit()