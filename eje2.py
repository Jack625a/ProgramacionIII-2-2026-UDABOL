class Animal:
    def __init__(self,color,especie):
        self.color=color
        self.especie=especie
    def comer(self,comida):
        print(f"esta comiendo {comida}")
    def dormir(self):
        print("Esta durmiendo...")

class AnimalDomestico(Animal):
    def __init__(self,color,especie,dueño,vacunas):
        super().__init__(color,especie)
        self.dueño=dueño
        self.vacunas=vacunas
    def pasear(self):
        print("esta paseando...")

class AnimalSalvaje(Animal):
    def __init__(self,color,especie,gradoAgresividad):
        super().__init__(color,especie)
        self.gradoAgresividad=gradoAgresividad
    def cazar(self):
        print("Esta cazando su comida...")

perro=AnimalDomestico("CAFE","Perro","Kevin","Completas")
leon=AnimalSalvaje("blanco","Leon","Alto")

perro.comer("carne")
leon.cazar()