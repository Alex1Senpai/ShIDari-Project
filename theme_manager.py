#theme_manager.py
import flet as ft

def create_theme_button(page: ft.Page):
    def toggle_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        icon_button.icon = ft.icons.WB_SUNNY if page.theme_mode == 'dark' else ft.icons.NIGHTS_STAY
        page.update()

    icon_button = ft.IconButton(
        icon=ft.icons.WB_SUNNY if page.theme_mode == 'dark' else ft.icons.NIGHTS_STAY,
        on_click=toggle_theme
    )
    return icon_button
