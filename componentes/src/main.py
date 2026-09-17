import flet as ft

from screens.pantalla1 import pantalla1Mostrar
from screens.pantalla2 import pantalla2Mostrar
from screens.pantalla3 import pantalla3Mostrar
from screens.pantalla4 import pantalla4Mostrar


def main(page: ft.Page):

    contenido=ft.Container(
        expand=True,
        padding=20
    )
    def cambiarPantalla(e):
        id=e.control.selected_index
        if id==0:
            contenido.content=pantalla1Mostrar()
        elif id==1:
            contenido.content=pantalla2Mostrar()
        elif id==2:
            contenido.content=pantalla3Mostrar()
        elif id==3:
            contenido.content=pantalla4Mostrar()

        contenido.update()

    page.bottom_appbar=ft.CupertinoNavigationBar(
        selected_index=0,
        on_change=cambiarPantalla,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.ABC,label="Productos"),
            ft.NavigationBarDestination(icon=ft.Icons.GPP_BAD,label="Servicios"),
            ft.NavigationBarDestination(icon=ft.Icons.AIR,label="Perfil")
        ],
        bgcolor="red"
    )


    page.add(
        contenido
       
    )


if __name__ == "__main__":
    ft.run(main)
