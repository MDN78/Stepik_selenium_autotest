# файл для переноса локаторов во внешнюю функцию
from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # теперь каждый селектор — это пара: как искать и что искать.

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class BookLocators():
    BUTTON_ADD_NEW_BOOK = (By.CSS_SELECTOR, "#add_to_basket_form")
    BOOK_NAME = (By.XPATH, "//div[@class='alertinner ']//strong")
    BOOK_PRICE = (By.XPATH, "//div[@class='icon-shopping-cart']//i")
