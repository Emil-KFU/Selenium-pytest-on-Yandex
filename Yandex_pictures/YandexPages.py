from BaseApp import BasePage
from selenium.webdriver.common.by import By

from urllib.parse import unquote

class YandexSearchLocators:
    # локатор для кнопки Меню
    LOCATOR_YANDEX_MENU_BUTTON = (By.XPATH, "//a[@title='Все сервисы']")
    # локатор для сервиса Картинки в Меню
    LOCATOR_YANDEX_IMAGES_IN_MENU = (By.XPATH, "//a[@aria-label='Картинки']")
    # локатор для первой категории на сайте https://ya.ru/images/
    LOCATOR_YANDEX_IMAGES_FIRST_CATEGORY = (By.CLASS_NAME, "PopularRequestList-Item.PopularRequestList-Item_pos_0")
    # локатор для 1 картинки после клика на 1 категорию на сайте https://ya.ru/images/
    LOCATOR_YANDEX_IMAGES_RESULTS_FIRST_IMAGE = (By.CLASS_NAME, "serp-item.serp-item_type_search.serp-item_group_search.serp-item_pos_0")
    # локатор для открывшегося окна с картинкой
    LOCATOR_YANDEX_IMAGES_RESULTS_FIRST_IMAGE_WINDOW = (By.CLASS_NAME, "MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container")
    # локатор для кнопки Вперёд
    LOCATOR_YANDEX_IMAGES_RESULTS_FIRST_IMAGE_WINDOW_FORWARD_BUTTON = (By.XPATH, "/html/body/div[14]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div[4]")
    # локатор для картинки в окне
    LOCATOR_YANDEX_IMAGES_RESULTS_CURRENT_IMAGE = (By.XPATH, "/html/body/div[14]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[5]/img")
    # локатор для кнопки Назад
    LOCATOR_YANDEX_IMAGES_RESULTS_IMAGE_WINDOW_PREV_BUTTON = (By.XPATH, "/html/body/div[14]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div[1]")
    
    # локатор для поля поиска:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    
class SearchHelper(BasePage):
    def click_on_search_field(self):
        # получим элемент "поле поиска" и кликнем на него
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time = 30).click()
    
    def check_menu_button(self):
        # получим элемент Меню, если он виден пользователю
        return self.find_element_by_visibility(YandexSearchLocators.LOCATOR_YANDEX_MENU_BUTTON)

    def go_to_images_page(self):
        # Нажмём на кнопку Меню
        self.find_element_by_visibility(YandexSearchLocators.LOCATOR_YANDEX_MENU_BUTTON, time = 30).click()
        # Нажмём на сервис Картинки в Меню
        images_element = self.find_element_by_visibility(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_IN_MENU).click()
        return images_element

    def images_first_category_click_and_name(self):
        # Получим название 1 категории
        name = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_FIRST_CATEGORY, time = 30).get_attribute("data-grid-text")
        # Нажмём на 1 категорию на ya.ru/images/
        self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_FIRST_CATEGORY, time = 30).click()
        return name

    def get_search_field_text(self):
        search_text = unquote(self.driver.current_url).replace('https://ya.ru/images/search?nl=1&source=morda&text=', '')
        return search_text

    def images_first_category_click(self):
        # Нажмём на 1 категорию на ya.ru/images/
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_FIRST_CATEGORY, time = 30).click()
 
    def open_first_image(self):
        # Откроем 1 картинку
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_RESULTS_FIRST_IMAGE, time = 30).click()
       
    def check_first_image_opened(self):
        # Получим окно с картинкой, если оно открылось
        return self.find_element_by_visibility(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_RESULTS_FIRST_IMAGE_WINDOW, time = 30)

    def next_button_click(self):
        # Нажмём на кнопку Вперёд
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_RESULTS_FIRST_IMAGE_WINDOW_FORWARD_BUTTON, time = 30).click()
    
    def current_image_src(self):
        # Получим атрибут src текущей картинки
        return self.find_element_by_visibility(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_RESULTS_CURRENT_IMAGE, time = 30).get_attribute("src")

    def prev_button_click(self):
        # Нажмём на кнопку Назад
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGES_RESULTS_IMAGE_WINDOW_PREV_BUTTON, time = 30).click()
