import pytest
from pages.product_page import AddNewBook
from pages.base_page import BasePage
from pages.login_page import LoginPage

# ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"



@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_can_add_product_to_basket(browser, link):
    print("Test 1\n")
    page = AddNewBook(browser, link)
    page.open()
    page.add_new_book_to_basket()
    page.solve_quiz_and_get_code()
    book_title = AddNewBook(browser, browser.current_url)
    book_title.is_title_right()
    book_title.is_price_right()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    print("Test 2\n")
    page = AddNewBook(browser, link)
    page.open()
    page.add_new_book_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message(browser, link):
    print("Test 3\n")
    page = AddNewBook(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    print("Test 4\n")
    page = AddNewBook(browser, link)
    page.open()
    page.add_new_book_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_success_message()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_should_see_login_link_on_product_page(browser, link):
    print("Test 5\n")
    page = AddNewBook(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    print("Test 6\n")
    page = AddNewBook(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/"])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    print("Test 7\n")
    page = BasePage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()
    page.should_be_empty_basket()



