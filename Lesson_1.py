import flet as ft # Импортируем и переимениуем (сокращаем на ft)

# Создание Страницы С помощью 
def main_page(page: ft.Page):

    # Создаем и задаем тему для страницы
    page.theme_mode = ft.ThemeMode.LIGHT
    
    #
    page.title = 'Мое первое приложение'
    #
    greteng = ft.Text(value="Hello")
    #
    name_input = ft.TextField(label="Введите имя:")
    #
    page.add(greteng, name_input)

#
ft.app(main_page)

# ft.app(main_page , view = ft.AppView.WEB_BROWSER)