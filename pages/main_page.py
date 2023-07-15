from .base_page import BasePage
from .locators import MainPageLocators

# Класс MainPage - является наследником класса BasePage
class MainPage(BasePage):
    """Установка заглушки тк функции перенесли в base_page"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

