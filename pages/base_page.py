from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # добавим команду для неявного ожидания со значением по умолчанию в 10
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

# Теперь в этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение.
# В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

