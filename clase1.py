#paso 1. definir la clase
class Persona:
    #paso 2. definir los atributos
    def __init__(self,nombre,ci):
        self.nombre=nombre
        self.ci=ci
    #paso 3. definir metodos
    def dormir(self):
        print(f"{self.nombre} esta durmiendo")

persona1=Persona("Kevin Arroyo",7545112)
persona1.dormir()