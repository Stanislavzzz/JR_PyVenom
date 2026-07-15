import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import config


def create_driver():
    """Создаем объект настроек Chrome."""
    chrome_options = Options()

    if config.USE_HEADLESS:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)

    return driver


def get_products(driver):
    """Функция для сбора товаров."""
    products = []

    return products


def load_more(driver, wait):
    """Функция для нажатия на кнопку More."""
    return False


def save_to_csv(products, filename):
    """Сохраняет товары в CSV."""
    with open(filename, "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=config.FIELD_NAMES)
        writer.writeheader()
        writer.writerows(products)


def save_to_excel(products, filename):
    """Сохраняет товары в CSV."""
    df = pd.DataFrame(products)
    df.to_excel(filename, index=False)


def main():
    """Главная функция."""
    driver = create_driver()
    wait = WebDriverWait(driver, config.WAIT_TIMEOUT)

    all_products = []

    try:
        driver.get(config.START_URL)
    finally:
        driver.quit()



if __name__ == '__main__':
    main()


