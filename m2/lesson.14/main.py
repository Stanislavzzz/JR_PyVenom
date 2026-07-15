import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import config


def create_driver():
    """Создаем объект настроек Chrome."""
    chrome_options = Options()

    if config.USE_HEADLESS:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--window-position=3500,0')
    chrome_options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=chrome_options)

    return driver


def get_products(driver):
    """Функция для сбора товаров."""
    product_cards = driver.find_elements(By.CSS_SELECTOR, config.PRODUCT_CARD_SELECTOR)

    products = []

    for card in product_cards:
        title_elements = card.find_elements(By.CSS_SELECTOR, config.TITLE_SELECTOR)

        if title_elements:
            title_element = title_elements[0]
            title = title_element.get_attribute("title")

            if not title:
                title = title_element.text.strip()

            url = title_element.get_attribute("href")
        else:
            title = ""
            url = ""

        price_elements = card.find_elements(By.CSS_SELECTOR, config.PRICE_SELECTOR)
        if price_elements:
            price = price_elements[0].text.strip()
        else:
            price = ""

        description_elements = card.find_elements(By.CSS_SELECTOR, config.DESCRIPTION_SELECTOR)
        if description_elements:
            description = description_elements[0].text.strip()
        else:
            description = ""

        product_data = {
            "title": title,
            "url": url,
            "price": price,
            "description": description
        }
        products.append(product_data)

    return products


def accept_cookies(driver):
    """Принимаем cookie-баннер, если он появился."""
    try:
        short_wait = WebDriverWait(driver, 3)

        accept_button = short_wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.BUTTON_ACCEPT))
        )

        driver.execute_script("arguments[0].click();", accept_button)

        print("Cookie-баннер закрыт")

    except TimeoutException:
        print("Cookie-баннер не появился")

    except WebDriverException as error:
        print("Не удалось закрыть cookie-баннер")
        print(error)


def load_more(driver, wait):
    """Функция для нажатия на кнопку More."""
    product_cars = driver.find_elements(By.CSS_SELECTOR, config.PRODUCT_CARD_SELECTOR)
    old_count = len(product_cars)


    try:
        accept_cookies(driver)

        load_more_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, config.LOAD_MORE_SELECTOR))
        )
        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            load_more_button,
        )
        load_more_button.click()

        # load_accept_button = wait.until(
        #     EC.element_to_be_clickable((By.XPATH, config.BUTTON_ACCEPT))
        # )
        # load_accept_button.click()

        wait.until(
            lambda browser: len(
                browser.find_elements(By.CSS_SELECTOR, config.PRODUCT_CARD_SELECTOR)
            ) > old_count
        )
        print("More нажали и загрузили товары")
        return True
    except TimeoutException:
        print("Не удалось дождаться кнопки Load More или новых товаров")
        return False
    except WebDriverException as error:
        print("Ошибка Selenium при попытке нажать More")
        print(error)
        return False



def save_to_csv(products, filename):
    """Сохраняет товары в CSV."""
    with open(filename, "w", newline='', encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=config.FIELD_NAMES)
        writer.writeheader()
        writer.writerows(products)


def save_to_excel(products, filename):
    """Сохраняет товары в Excel."""
    df = pd.DataFrame(products)
    df.to_excel(filename, index=False)


def main():
    """Главная функция."""
    driver = create_driver()

    wait = WebDriverWait(driver, config.WAIT_TIMEOUT)

    all_products = []

    try:
        driver.get(config.START_URL)
        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, config.PRODUCT_CARD_SELECTOR))
        )
        products = get_products(driver)
        all_products.extend(products)
        print(f"Товаров после первой загрузки {len(all_products)}")

        for click_num in range(config.MAX_LOAD_MORE_CLICKS):
            is_load_more = load_more(driver, wait)

            if not is_load_more:
                print("Больше товаров подгрузить не удалось")
                break

            products = get_products(driver)
            all_products = products
            print(f"Клик {click_num + 1}. Всего товаров {len(all_products)}")

        save_to_csv(all_products, config.CSV_FILENAME)
        print("Данные сохранены в CSV")
        save_to_excel(all_products, config.EXCEL_FILENAME)
        print("Данные сохранены в EXCEL")

        print(f"Всего товаров {len(all_products)}")

    finally:
        driver.quit()


if __name__ == '__main__':
    main()
