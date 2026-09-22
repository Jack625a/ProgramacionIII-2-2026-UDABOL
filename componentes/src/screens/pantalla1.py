import flet as ft

def pantalla1Mostrar():
    return ft.Column(
        controls=[
            ft.Text("Pantalla 1",
                    size=30),
            ft.Image(src="https://1000marcas.net/wp-content/uploads/2020/11/Python-logo.png"),
            ft.ListView(
                controls=[
                    ft.Text("Dato1",size=20),
                    ft.Text("Dato2",size=20),
                    ft.Text("Dato3",size=20),
                   
                ],
                #horizontal=True,
                spacing=15,
                
            ),
            ft.Checkbox(label="Opcion1"),
            ft.Checkbox(label="Opcion2"),
            ft.RadioGroup(
                content=ft.Column(
                    controls=
                     [
                        ft.Radio(label="Opcion 3"),
                        ft.Radio(label="Opcion 4"),
                        ft.Radio(label="Opcion5")
                    ]                           
                    )

                ),
            ft.Dropdown(
                label="Seleccione su carrera",
                options=[
                    ft.DropdownOption(key="sistemas",text="Ingenieria de Sistemas",leading_icon=ft.Icons.LAPTOP),
                    ft.DropdownOption(key="derecho", text="Derecho",leading_icon=ft.Icons.BALANCE),
                    ft.DropdownOption(key="medicina", text="Medicina",leading_icon=ft.Icons.MEDICAL_INFORMATION)
                ],
                bgcolor="yellow",
                leading_icon=ft.Icons.LIST,

                        )

               
        
            
            
        ]
    )