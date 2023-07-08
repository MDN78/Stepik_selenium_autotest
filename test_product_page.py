from pages.product_page import AddNewBook

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = AddNewBook(browser, link)
    page.open()
    page.add_new_book_to_basket()
    page.solve_quiz_and_get_code()
    book_title = AddNewBook(browser, browser.current_url)
    book_title.is_title_right()
    book_title.is_price_right()






