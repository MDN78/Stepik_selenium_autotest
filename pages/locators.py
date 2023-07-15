# файл для переноса локаторов во внешнюю функцию
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # теперь каждый селектор — это пара: как искать и что искать.

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")

class BookLocators():
    BUTTON_ADD_NEW_BOOK = (By.CSS_SELECTOR, "#add_to_basket_form")
    BOOK_NAME = (By.XPATH, "//ul[@class='breadcrumb']//li[@class='active']")
    BOOK_ALERT_NAME = (By.XPATH, "//div[@class='alertinner ']//strong")
    BOOK_PUBLICK_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
    BOOK_BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']//p//strong")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']//div[@class='alertinner ']")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class,basket-mini)]/span[@class='btn-group']/a[contains(@href, 'basket')]")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
