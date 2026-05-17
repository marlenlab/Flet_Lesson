import flet as ft # Импортируем и переимениуем (сокращаем на ft)

# Создание Страницы С помощью 
def main_page(page: ft.Page):

    # Создаем и задаем тему для страницы
    page.theme_mode = ft.ThemeMode.LIGHT

    # Даем название страницы
    page.title = 'Мое первое приложение'
    
    hello_text = ft.Text("Hello World")

    greeting_histori = []

    histori_text = ft.Text('История приветствий')




    # # Добавлям текст  в страницу
    # greeting = ft.Text(value="Hello")

    def on_button_click(_):

        name = name_input.value.strip()

        if name:
            hello_text.color = None
            hello_text.value = f'Hello {name}'
            name_input.value = None

            greeting_histori.append(name)
            print(greeting_histori)
            histori_text.value = 'История приветствий: \n' + '\n' .join(greeting_histori)
        else:
            hello_text.value = "Ошибка! Введите имя!!!"
            hello_text.color = ft.Colors.RED
        
        
        page.update()

    # Создаем введение имени через страницу
    name_input = ft.TextField(label="Введите имя:", on_submit = on_button_click)

    # 3D кнопка
    elevated_button = ft.ElevatedButton('SEND', icon=ft.Icons.SEND, on_click= on_button_click )



    # Обычная кнопка
    # text_button = ft.TextButton('SEND', icon=ft.Icons.SEND)

    # Кнопка иконка
    # icon_button = ft.IconButton(icon=ft.Icons.SEND)

    def on_clear_button(_):
        greeting_histori.clear()
        histori_text.value = 'История приветствий'
        page.update()

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=on_clear_button)



    
    # Добавляем элементы в страницы чтоб они работали
    page.add(hello_text, name_input, elevated_button, histori_text, clear_button )

# text_button, icon_button

# Для запуска
ft.app(main_page)

# Для запуска через браузер
# ft.app(main_page , view = ft.AppView.WEB_BROWSER)