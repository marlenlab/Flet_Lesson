import flet as ft # Импортируем и переимениуем (сокращаем на ft)

# Создание Страницы С помощью 
def main_page(page: ft.Page):

    # Создаем и задаем тему для страницы
    page.theme_mode = ft.ThemeMode.LIGHT

    # Даем название страницы
    page.title = 'Мое первое приложение'

    # Добавлям текст  в страницу
    greteng = ft.Text(value="Hello")

    # Создаем введение имени через страницу
    name_input = ft.TextField(label="Введите имя:")
    
    # Добавляем элементы в страницы чтоб они работали
    page.add(greteng, name_input)

# Для запуска
ft.app(main_page)

# Для запуска через браузер
# ft.app(main_page , view = ft.AppView.WEB_BROWSER)