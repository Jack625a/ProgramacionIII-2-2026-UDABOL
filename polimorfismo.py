class Animal:
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie
    def comer(self,comida):
        print(f"Esta comiendo {comida}")
    def hacerSonido(self):
        print("Esta haciendo un sonido...")

class AnimalDomestico(Animal):
    def __init__(self,color,especie,nombre,dueño):
        super().__init__(color,especie)
        self.nombre=nombre
        self.dueño=dueño
    def pasear(self):
        print("Esta paseando...")
    def hacerSonido(self,sonido):
        print(f"Esta {sonido}")

perro=AnimalDomestico("blanco","perro","scott","kevin")
perro.hacerSonido("Ladrando")
gato=AnimalDomestico("cafe","gato","srbigotes","juan")
gato.hacerSonido("maullando")