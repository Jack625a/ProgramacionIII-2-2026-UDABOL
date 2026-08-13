#Paso 1. Definir la clase
class Animal:
    #Paso 2. Definir las propiedades
    def __init__(self,color,especie,genero,habitad):
        self.color=color
        self.especie=especie
        self.genero=genero
        self.habitad=habitad
    #Paso 3. Definir las acciones o metodos
    def comer(self,comida):
        print(f"{self.especie} Esta comiendo {comida}")
    def reproducirse(self):
        print(f"Se esta reproduciendo")
    def dormir(self):
        print(f"Esta durmiendo {self.especie}")

#Paso 4. Definir los objetos de la clase
oso=Animal("cafe","oso","macho","bosques")
caballoMar=Animal("rosado","caballo de mar","hembra","mar")
perro=Animal("blanco","perro","macho","ciudad")

oso.dormir()
caballoMar.comer("algas")
oso.comer("bambu")
perro.reproducirse()