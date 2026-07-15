# START_URL = "https://webscraper.io/test-sites/load-more"
START_URL = "https://webscraper.io/test-sites/e-commerce/more/computers/tablets"
CSV_FILENAME = "products.csv"
EXCEL_FILENAME = "products.xlsx"
FIELD_NAMES = [
    "title",
    "url",
    "price",
    "description",

]

PRODUCT_CARD_SELECTOR = ".thumbnail"
TITLE_SELECTOR = "a.title"
PRICE_SELECTOR = ".price"
DESCRIPTION_SELECTOR = ".description"
LOAD_MORE_SELECTOR = "a.ecomerce-items-scroll-more"
BUTTON_ACCEPT = "button[data-tid='banner-accept']"

USE_HEADLESS = False
WAIT_TIMEOUT = 10
MAX_LOAD_MORE_CLICKS = 5