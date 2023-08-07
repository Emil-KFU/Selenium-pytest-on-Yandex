# Selenium-pytest-on-Yandex
Выполнены автотесты на языке Python с помощю библиотек pytest и Selenium на примере поисковой страницы Яндекса и страницы с картинками (ya.ru/images/).
Проект выполнен в соответствии с паттерном Page Object.

# Поиск в Яндексе
1)	Зайти на https://ya.ru/
2)	Проверить наличия поля поиска
3)	Ввести в поиск Тензор
4)	Проверить, что появилась таблица с подсказками (suggest) 
5)	Нажать enter
6)	Проверить, что появилась страница результатов поиска
7)	Проверить 1 ссылка ведет на сайт tensor.ru

# Картинки на Яндексе
1)	Зайти на ya.ru
2)	Проверить, что кнопка меню присутствует на странице (В моей версии Яндекса её нет, чтобы она появилась надо нажать на поле поиска)
3)	Открыть меню, выбрать “Картинки”
4)	Проверить, что перешли на url https://yandex.ru/images/ (сейчас он https://ya.ru/images/)
5)	Открыть первую категорию
6)	Проверить, что название категории отображается в поле поиска
7)	Открыть 1 картинку
8)	Проверить, что картинка открылась
9)	Нажать кнопку вперед
10)	Проверить, что картинка сменилась
11)	Нажать назад
12)	Проверить, что картинка осталась из шага 8
