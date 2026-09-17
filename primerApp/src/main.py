import flet as ft #importacion de la libreria

def main(page: ft.Page): #funcion principal


    page.bottom_appbar=ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME,label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.FACE,label="Perfil"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS,label="Ajustes")
        ],
        bgcolor="yellow"
    )

    boton1=ft.Button("Boton Clase",icon=ft.Icons.TIKTOK,width=250)
    boton2=ft.CupertinoFilledButton("Boton Subclase",icon=ft.Icons.FACE,bgcolor="green")
    boton3=ft.ElevatedButton("Boton Elevated",bgcolor="yellow")
    boton4=ft.OutlinedButton("Boton Bordes")
    boton5=ft.FilledButton("Boton Filled")
    boton6=ft.CupertinoButton("Boton Cupertino",bgcolor="red")
    imagen=ft.Image("https://i.ytimg.com/vi/pxfcYpsr-gA/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDtrXkOk12BmeudR9vSbcCTnRnhjw",border_radius=ft.BorderRadius(50,50,20,20))

    page.add( #interfaz
        imagen,
        boton1,
        boton2,
        boton3,
        boton4,
        boton5,
        boton6
        
    )

ft.run(main)
