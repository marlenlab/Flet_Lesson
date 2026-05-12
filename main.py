import flet as ft

def main_page(page: ft.Page):
    #Hello_Text = 'Hello Gekss'
    page.title = 'My first Project'
    page.theme_mode = ft.ThemeMode.LIGHT

    Hello_Text = ft.Text(value='Hello, World')

    name_input = ft.TextField(label='Введите имя')


    page.add(Hello_Text, name_input)
    
ft.app(main_page)
#ft.app(main_page, view=ft.AppView.WEB_BROWSER)