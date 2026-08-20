#Paso1. Crear la clase
class Automovil:
    #Paso2. Definir los atributos
    def __init__(self,marca,modelo,año):
        self.marca=marca
        self.modelo=modelo
        self.año=año
    #Paso3. Definir las acciones
    def acelerar(self):
        print("Esta acelerando...")
    def frenar(self):
        print("Frenando...")

class AutoElectrico(Automovil):
    def __init__(self,marca,modelo,año,porcentajeBateria,sensor):
        super().__init__(marca,modelo,año)
        self.porcentajeBateria=porcentajeBateria
        self.sensor=sensor

    def activarPilotAutomatico(self):
        print("Se activo el piloto automatico...")

auto1=AutoElectrico("Tesla","CyberTruck","2026","100%","Distancia")
auto1.activarPilotAutomatico()
auto1.acelerar()
