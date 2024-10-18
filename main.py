import webbrowser
import flet as ft
from theme_manager import create_theme_button
from navigation import create_navigation_drawer
from content import load_content

def open_map():
    webbrowser.open('path_to_your_map.html')  # Замените на путь к вашему файлу map.html

def main(page: ft.Page):
    page.title = "ShiDari App"
    page.theme_mode = 'dark'

    # Область контента
    content_area = ft.Column()

    # Функция для обновления контента
    def update_content(view, page):
        content_area.controls.clear()  # Очищаем существующий контент
        content_area.controls.extend(load_content(view, page))  # Передаем page
        navigation_drawer.open = False
        page.update()

    # Создаем NavigationDrawer
    navigation_drawer = create_navigation_drawer(update_content, page)

    # Функция для открытия NavigationDrawer
    def open_drawer(e):
        navigation_drawer.open = True
        page.update()

    # Создаем AppBar
    app_bar = ft.AppBar(
        title=ft.Text("ShiDari App"),
        actions=[create_theme_button(page)],  # Передаем страницу как аргумент
        leading=ft.IconButton(icon=ft.icons.MENU, on_click=open_drawer),
        bgcolor=ft.colors.BLUE_500
    )

    # Устанавливаем NavigationDrawer на страницу
    page.drawer = navigation_drawer

    # Добавляем AppBar и область контента на страницу
    page.add(app_bar, content_area)

    # Загружаем главную страницу по умолчанию
    update_content("home", page)

ft.app(target=main)
