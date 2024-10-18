#navigation.py
import flet as ft

def create_navigation_drawer(load_content, page):
    navigation_drawer = ft.NavigationDrawer(
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Image(src="C:/Users/Administrator/Desktop/ShIDari Project/imgs/inf.png", width=70, height=70),
                        alignment=ft.alignment.center,
                        padding=ft.padding.all(5),
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.HOME),
                        title=ft.Text("Главная"),
                        on_click=lambda e: load_content("home", page)  # Передаем page
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.CALCULATE_OUTLINED),
                        title=ft.Text("Калькулятор"),
                        on_click=lambda e: load_content("calculator", page)  # Передаем page
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.MAP),
                        title=ft.Text("Карта"),
                        on_click=lambda e: load_content("map", page)  # Передаем page
                    ),
                    ft.ListTile(
                        leading=ft.Icon(ft.icons.CURRENCY_BITCOIN),
                        title=ft.Text("Курс BTC"),
                        on_click=lambda e: load_content("btc", page)  # Передаем page
                    ),
                ]
            )
        ]
    )
    return navigation_drawer
