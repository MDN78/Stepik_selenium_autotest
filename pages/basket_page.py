from .locators import BasePageLocators

class BasketPage:
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEM), "Basket is not empty"