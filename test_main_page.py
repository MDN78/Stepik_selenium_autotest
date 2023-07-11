from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page(browser):
    print("Test 1\n")
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.go_to_login_page()         # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)  # пошли проверки login_page
    login_page.should_be_login_page()


def test_guest_should_be_see_login_link(browser):
    print("Test 2\n")
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    print("Test 3\n")
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.guest_clik_button_see_basket()
    page.should_be_empty_basket()

# start test: pytest -v --tb=line --browser_name=chrome --language=en test_main_page.py
# start test option 2 - pytest -s test_main_page.py
