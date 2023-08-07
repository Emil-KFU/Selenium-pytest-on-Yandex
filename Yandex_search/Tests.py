from YandexPages import SearchHelper
import time
import urllib

def test_yandex_search_field(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    yandex_main_page = SearchHelper(browser)
    # Заходим на сайт ya.ru
    yandex_main_page.go_to_site()
    # Проверяем наличие поля поиска
    yandex_main_page.check_search_field()

def test_yandex_suggest_table(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    # Вводим в поле поиска поиска слово "Тензор"
    yandex_main_page.enter_word("Тензор")
    # Проверяем наличие поля поиска
    yandex_main_page.check_suggest_table()

def test_yandex_search_results_page(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.enter_word("\n")
    # Создаём объект, соответствующий странице результатов поиска
    yandex_search_results_page = SearchHelper(browser)
    yandex_search_results_page.driver.get(yandex_main_page.driver.current_url)
    # Проверяем, что создан список с результатами поиска
    yandex_search_results_page.check_search_results_page()

def test_yandex_search_results_first_link(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.enter_word("\n")
    # Создаём объект, соответствующий странице результатов поиска
    yandex_search_results_page = SearchHelper(browser)
    yandex_search_results_page.driver.get(yandex_main_page.driver.current_url)
    # Проверяем, что 1 ссылка в результатах поиска имеет адрес tensor.ru
    href = yandex_search_results_page.check_search_results_first_link()
    assert "https://tensor.ru/" == href
