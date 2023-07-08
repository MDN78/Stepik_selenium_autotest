from .base_page import BasePage
from .locators import BookLocators
from selenium.webdriver.common.by import By

class AddNewBook(BasePage):
        def add_new_book_to_basket(self):
            add_book = self.browser.find_element(*BookLocators.BUTTON_ADD_NEW_BOOK)
            add_book.click()

        def should_be_book_title(self):
            assert self.is_element_present(*BookLocators.BOOK_NAME), "Book name is not presented"

        def should_be_book_price(self):
            assert self.is_element_present(*BookLocators.BOOK_PRICE), "Book price is not presented"

            # By.XPATH, "//ul[@class='breadcrumb']//li[@class='active']//"
        def is_title_right(self):
            breadcrumb_title = self.browser.find_element(By.XPATH, "//ul[@class='breadcrumb']//li[@class='active']")
            book_title = breadcrumb_title.text
            alert_title = self.browser.find_element(By.XPATH, "//div[@class='alertinner ']//strong")
            book_title_alert = alert_title.text
            assert book_title == book_title_alert, "Book name is wrong"

        def is_price_right(self):
            publick_price = self.browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']//p[@class='price_color']")
            book_price = publick_price.text
            second_price = self.browser.find_element(By.XPATH, "//div[@class='alertinner ']//p//strong")
            basket_price = second_price.text
            assert book_price == basket_price, "Wrong price!"


