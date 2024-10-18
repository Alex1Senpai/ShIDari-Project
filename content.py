#content.py
import flet as ft
import requests  # Для работы с API

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, on_click=None, expand=1):
        super().__init__(text=text, on_click=on_click, expand=expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.BLACK

def load_content(view, page):
    if view == "home":
        return [ft.Text("Добро пожаловать в ShiDari App! Здесь вы можете использовать калькулятор, посмотреть карту и узнать текущий курс BTC.")]
    
    elif view == "calculator":
        return calculator_interface(page)

    elif view == "map":
        return [ft.Text("Здесь будет карта.")]  # Место для карты

    elif view == "btc":
        return btc_price_interface()

    return []

def calculator_interface(page):
    # Создаем поле для отображения результата
    result = ft.TextField(label="", read_only=True, width=300, text_align="right", text_size=20)

    # Логика для вычислений
    expression = ""

    def button_click(value):
        nonlocal expression
        expression += value
        result.value = expression
        page.update()

    def calculate(e):
        nonlocal expression
        try:
            expression = str(eval(expression))
            result.value = expression
        except Exception:
            result.value = "Ошибка"
            expression = ""
        page.update()

    def clear(e):
        nonlocal expression
        expression = ""
        result.value = ""
        page.update()

    def backspace(e):
        nonlocal expression
        expression = expression[:-1]  # Удаляем последний символ
        result.value = expression
        page.update()

    # Определяем кнопки
    buttons = [
        ("C", clear), ("/", lambda e: button_click("/")), ("*", lambda e: button_click("*")), ("BS", backspace),
        ("7", lambda e: button_click("7")), ("8", lambda e: button_click("8")), ("9", lambda e: button_click("-")),
        ("4", lambda e: button_click("4")), ("5", lambda e: button_click("5")), ("6", lambda e: button_click("+")),
        ("1", lambda e: button_click("1")), ("2", lambda e: button_click("2")), ("3", lambda e: button_click("3")),
        ("%", lambda e: button_click("%")), ("0", lambda e: button_click("0")), (",", lambda e: button_click(".")),
    ]

    # Формируем ряды кнопок
    button_rows = [
        ft.Row(controls=[CalcButton(text=buttons[i][0], on_click=buttons[i][1]) for i in range(0, 4)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[CalcButton(text=buttons[i][0], on_click=buttons[i][1]) for i in range(4, 8)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[CalcButton(text=buttons[i][0], on_click=buttons[i][1]) for i in range(8, 12)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[
            CalcButton(text="=", on_click=calculate),  # Кнопка "="
            ft.Container(height=60),  # Пустой контейнер для создания вертикального пространства
        ], alignment=ft.MainAxisAlignment.CENTER),
    ]

    # Центрируем все элементы
    container = ft.Column(
        controls=[
            ft.Container(
                content=result,
                alignment=ft.alignment.center,
                padding=ft.padding.symmetric(vertical=20)
            ),
            *button_rows  # Распаковываем ряды кнопок
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    return [container]

def btc_price_interface():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        data = response.json()
        price = data["bpi"]["USD"]["rate"]
        return [ft.Text(f"Текущий курс BTC: ${price} USD")]
    except Exception:
        return [ft.Text("Не удалось получить курс BTC.")]
