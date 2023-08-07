from YandexPages import SearchHelper
import time
import urllib

def test_yandex_menu_button(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    yandex_main_page = SearchHelper(browser)
    # Заходим на сайт ya.ru
    yandex_main_page.go_to_site()
    # Кликаем на поле поиска, чтобы появилась кнопка Меню
    yandex_main_page.click_on_search_field()
    # Проверяем, что появилась кнопка Меню
    assert yandex_main_page.check_menu_button() != None

def test_yandex_images_url(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    yandex_main_page = SearchHelper(browser)
    # Заходим на сайт ya.ru
    yandex_main_page.go_to_site()
    # Кликаем на поле поиска, чтобы появилась кнопка Меню
    yandex_main_page.click_on_search_field()
    # Кликаем на кнопку Меню, затем на сервис Картинки
    yandex_main_page.go_to_images_page()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[1])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_page = SearchHelper(browser)
    # Проверяем, что перешли на url https://ya.ru/images/
    assert "https://ya.ru/images/" == yandex_images_page.driver.current_url

def test_yandex_images_first_category_in_search_field(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    yandex_main_page = SearchHelper(browser)
    # Заходим на сайт ya.ru
    yandex_main_page.go_to_site()
    # Кликаем на поле поиска, чтобы появилась кнопка Меню
    yandex_main_page.click_on_search_field()
    # Кликаем на кнопку Меню, затем на сервис Картинки
    yandex_main_page.go_to_images_page()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[2])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_page = SearchHelper(browser)
    first_category_name = yandex_images_page.images_first_category_click_and_name()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[2])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_result_page = SearchHelper(browser)
    search_field_text = yandex_images_result_page.get_search_field_text()
    time.sleep(5)
    assert first_category_name == search_field_text
    
def test_yandex_images_results_first_image_opened(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    yandex_main_page = SearchHelper(browser)
    # Заходим на сайт ya.ru
    yandex_main_page.go_to_site()
    # Кликаем на поле поиска, чтобы появилась кнопка Меню
    yandex_main_page.click_on_search_field()
    # Кликаем на кнопку Меню, затем на сервис Картинки
    yandex_main_page.go_to_images_page()
    
    # Переключаемся на новую вкладку браузера с url ya.ru/images/ по её window_handle
    browser.switch_to.window(browser.window_handles[3])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_page = SearchHelper(browser)
    yandex_images_page.images_first_category_click()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[3])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_result_page = SearchHelper(browser)
    yandex_images_result_page.open_first_image()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[3])
    # Создаём объект, соответствующий открытой веб-странице с окном первой картинки
    yandex_images_results_window = SearchHelper(browser)
    time.sleep(5)
    assert yandex_images_results_window.check_first_image_opened() != None
   
def test_yandex_images_results_image_changed(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    yandex_main_page = SearchHelper(browser)
    # Заходим на сайт ya.ru
    yandex_main_page.go_to_site()
    # Кликаем на поле поиска, чтобы появилась кнопка Меню
    yandex_main_page.click_on_search_field()
    # Кликаем на кнопку Меню, затем на сервис Картинки
    yandex_main_page.go_to_images_page()
    
    # Переключаемся на новую вкладку браузера с url ya.ru/images/ по её window_handle
    browser.switch_to.window(browser.window_handles[4])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_page = SearchHelper(browser)
    yandex_images_page.images_first_category_click()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[4])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_result_page = SearchHelper(browser)
    yandex_images_result_page.open_first_image()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[4])
    # Создаём объект, соответствующий открытой веб-странице с окном первой картинки
    yandex_images_results_window = SearchHelper(browser)
    # Сохраняем атрибут src первой картинки в переменную
    first_image_src = yandex_images_results_window.current_image_src()
    yandex_images_results_window.next_button_click()

    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[4])
    # Создаём объект, соответствующий открытой веб-странице с окном второй картинки
    yandex_images_results_second_image_window = SearchHelper(browser)
    time.sleep(5)
    # Сохраняем атрибут src 2 картинки в переменную 
    second_image_src = yandex_images_results_second_image_window.current_image_src()
    # Сравниваем 2 src между собой
    assert first_image_src != second_image_src

def test_yandex_images_results_image_returned(browser):
    # Создаём объект, соответствующий веб-странице (согласно паттерну Page Object)
    yandex_main_page = SearchHelper(browser)
    # Заходим на сайт ya.ru
    yandex_main_page.go_to_site()
    # Кликаем на поле поиска, чтобы появилась кнопка Меню
    yandex_main_page.click_on_search_field()
    # Кликаем на кнопку Меню, затем на сервис Картинки
    yandex_main_page.go_to_images_page()
    
    # Переключаемся на новую вкладку браузера с url ya.ru/images/ по её window_handle
    browser.switch_to.window(browser.window_handles[5])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_page = SearchHelper(browser)
    yandex_images_page.images_first_category_click()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[5])
    # Создаём объект, соответствующий открытой веб-странице
    yandex_images_result_page = SearchHelper(browser)
    yandex_images_result_page.open_first_image()
    
    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[5])
    # Создаём объект, соответствующий открытой веб-странице с окном первой картинки
    yandex_images_results_window = SearchHelper(browser)
    # Сохраняем атрибут src первой картинки в переменную
    first_image_src = yandex_images_results_window.current_image_src()
    yandex_images_results_window.next_button_click()

    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[5])
    # Создаём объект, соответствующий открытой веб-странице с окном второй картинки
    yandex_images_results_second_image_window = SearchHelper(browser)
    yandex_images_results_second_image_window.prev_button_click()

    # Переключаемся на новую вкладку браузера по её window_handle
    browser.switch_to.window(browser.window_handles[5])
    # Создаём объект, соответствующий открытой веб-странице с окном третей (первой) картинки
    yandex_images_results_third_image_window = SearchHelper(browser)
    # Сохраняем атрибут src 3 картинки в переменную 
    third_image_src = yandex_images_results_third_image_window.current_image_src()
    assert first_image_src == third_image_src
