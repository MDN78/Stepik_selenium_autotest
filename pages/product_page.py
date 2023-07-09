from .base_page import BasePage
from .locators import BookLocators, ProductPageLocators

class AddNewBook(BasePage):
        def add_new_book_to_basket(self):
            add_book = self.browser.find_element(*BookLocators.BUTTON_ADD_NEW_BOOK)
            add_book.click()

        def is_title_right(self):
            breadcrumb_title = self.browser.find_element(*BookLocators.BOOK_NAME)
            book_title = breadcrumb_title.text
            alert_title = self.browser.find_element(*BookLocators.BOOK_ALERT_NAME)
            book_title_alert = alert_title.text
            assert book_title == book_title_alert, "Book name is wrong"

        def is_price_right(self):
            publick_price = self.browser.find_element(*BookLocators.BOOK_PUBLICK_PRICE)
            book_price = publick_price.text
            second_price = self.browser.find_element(*BookLocators.BOOK_BASKET_PRICE)
            basket_price = second_price.text
            assert book_price == basket_price, "Wrong price!"

        def should_not_be_success_message(self):
            assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"

        def should_be_disappeared_success_message(self):
            assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
               "Success message is presented, but should not be"