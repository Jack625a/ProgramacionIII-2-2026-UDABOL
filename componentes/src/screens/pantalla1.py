import flet as ft

def pantalla1Mostrar():
    return ft.Column(
        controls=[
            ft.Text("Pantalla 1",
                    size=30),
            ft.Image(src="https://1000marcas.net/wp-content/uploads/2020/11/Python-logo.png")
        ]
    )