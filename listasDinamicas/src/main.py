import flet as ft


def main(page: ft.Page):

    datos = {
        1: {
            "nombre": "Laptop",
            "precio": 4500,
            "imagen": "https://i.dell.com/is/image/DellContent//content/dam/images/products/laptops-and-2-in-1s/dell-laptop/db14250-non-touch/dell-db14250nt-laptop-c-22040rf115-bl-fpr.psd?qlt=95&fit=fit&hei=630&wid=1200&fmt=png-alpha"
        },
        2: {
            "nombre": "Celular",
            "precio": 3500,
            "imagen": "https://triplex.com.bo/wp-content/uploads/2025/04/subir-producto-web-1000x1000-3.jpg"
        },
        3: {
            "nombre": "Celular",
            "precio": 3500,
            "imagen": "https://triplex.com.bo/wp-content/uploads/2025/04/subir-producto-web-1000x1000-3.jpg"
        },
        4: {
            "nombre": "Celular",
            "precio": 3500,
            "imagen": "https://triplex.com.bo/wp-content/uploads/2025/04/subir-producto-web-1000x1000-3.jpg"
        }
    }

    lista = ft.ListView(
        spacing=10,
        expand=True,
        col=2

    )

    for id, producto in datos.items():

        tarjeta = ft.Container(
            content=ft.Column(
                [
                    ft.Image(
                        src=producto["imagen"],
                        width=200,
                        height=120
                    ),

                    ft.Column(
                        [
                            ft.Text(f"ID: {id}"),
                            ft.Text(
                                producto["nombre"],
                                size=22
                            ),
                            ft.Text(
                                f'Precio: {producto["precio"]} Bs'
                            )
                        ],
                        expand=True
                    ),

                    ft.ElevatedButton(
                        "Comprar"
                    )
                ]
            ),
            padding=10
        )

        
        lista.controls.append(tarjeta)

    page.add(lista)


ft.run(main)

