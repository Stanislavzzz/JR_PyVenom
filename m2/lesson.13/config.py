# START_URL = "https://webscraper.io/test-sites/load-more"
START_URL = "https://webscraper.io/test-sites/e-commerce/more/computers/tablets"
CSV_FILENAME = "products.csv"
EXCEL_FILENAME = "products.xlsx"
FIELD_NAMES = [
    "title",
    "price",
    "description",
    "rating",
    "reviews",
    "url"
]

PRODUCT_CARD_SELECTOR = ".thumbnail"
TITLE_SELECTOR = ".title"
PRICE_SELECTOR = ".price"
DESCRIPTION_SELECTOR = ".description"
LOAD_MORE_SELECTOR = ".ecomerce-items-scroll-more"

USE_HEADLESS = False
WAIT_TIMEOUT = 10
MAX_LOAD_MORE_CLICKS = 5