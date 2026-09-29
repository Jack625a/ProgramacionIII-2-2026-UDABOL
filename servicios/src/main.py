import flet as ft
import requests

firebaseConfig = {
 
}

apiKey=""


def main(page: ft.Page):

    email=ft.TextField(label="Ingrese su correo")
    password=ft.TextField(label="Ingrese su contraseña",password=True)
    mensaje=ft.Text()

    def registrarse(e):
        url=f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={apiKey}"

        datos={
            "email":email.value,
            "password":password.value,
            "returnSecureToken":True
        }
        respuesta=requests.post(url,json=datos)
        if respuesta.ok:
            mensaje.value="Cuenta creada..."
            email.value=""
            password.value=""

        else:
            mensaje.value="Error al crear la cuenta"
        page.update()

    page.add(
        ft.Text("Crear Cuenta"),
        email,
        password,
        ft.Button("Crear Cuenta", on_click=registrarse),
        mensaje
    )


ft.run(main)
