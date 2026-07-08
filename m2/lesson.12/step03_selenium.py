from selenium import webdriver
from selenium.webdriver.common.by import By  #By.CSS_SELECTOR  By.XPATH
import time

url = 'https://quotes.toscrape.com/'
driver = webdriver.Chrome()
driver.set_window_position(3500, 0)

try:
    driver.get(url)
    login_link = driver.find_element(By.XPATH, "//a[text()='Login']")
    login_link.click()
    time.sleep(2)
    user_input = driver.find_element(By.CSS_SELECTOR, "#username")
    user_input.send_keys('student')
    time.sleep(3)
    user_input.clear()
    time.sleep(3)
    user_input.send_keys('user')
    time.sleep(3)
    password_input = driver.find_element(By.CSS_SELECTOR, "#password")
    password_input.send_keys('pass123')
    time.sleep(3)
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
    submit_button.click()
    time.sleep(5)
finally:
    driver.quit()

print('Selenium WebDriver - OK!')
