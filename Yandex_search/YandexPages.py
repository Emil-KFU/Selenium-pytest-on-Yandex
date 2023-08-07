from BaseApp import BasePage
from selenium.webdriver.common.by import By

class YandexSearchLocators:
    # локатор для поля поиска:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    # локатор для таблицы с подсказками suggest
    LOCATOR_YANDEX_SUGGEST_TABLE = (By.CLASS_NAME, "mini-suggest__popup-content")
    # локатор для страницы результатов поиска
    LOCATOR_YANDEX_SEARCH_RESULTS_PAGE = (By.ID, "search-result")
    # локатор для тега a 1 ссылки списка результатов поиска со значением атрибута class равным 'Link'
    LOCATOR_YANDEX_SEARCH_RESULTS_FIRST_LINK = (By.XPATH, "//*[@id='search-result']/li[1]/div/div[2]/div[1]/a")
    
class SearchHelper(BasePage):

    def check_search_field(self):
        # получим элемент "поле поиска" по его локатору:
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time = 30)
    
    def enter_word(self, word):
        # получим элемент "поле поиска":
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        # кликнем на него
        search_field.click()
        # введём необходимое слово
        search_field.send_keys(word)
        return search_field

    def check_suggest_table(self):
        # получим таблицу с подсказками, если она видна пользователю
        return self.find_element_by_visibility(YandexSearchLocators.LOCATOR_YANDEX_SUGGEST_TABLE, time = 10)

    def check_search_results_page(self):
        # получим список с результатами поиска по его ID
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULTS_PAGE)

    def check_search_results_first_link(self):
        # получим значение атрибута href тега a 1 элемента списка с результатами поиска, в котором содержится ссылка на сайт
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_RESULTS_FIRST_LINK).get_attribute("href")
