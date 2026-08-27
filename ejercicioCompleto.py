class Persona:
    def __init__(self,nombre,ci,fechaNacimiento):
        self.nombre=nombre
        self.ci=ci
        self.fechaNacimiento=fechaNacimiento

    def hablar(self):
        print("Esta hablando...")

class Estudiante(Persona):
    def __init__(self,nombre,ci,fechaNacimiento,codEstudiante,carrera):
        super().__init__(nombre,ci,fechaNacimiento)
        self.codEstudiante=codEstudiante
        self.carrera=carrera
    def hablar(self):
        print("Esta hablando el estudiante en lenguaje cotidiano...")


class Docente(Persona):
    def __init__(self,nombre,ci,fechaNacimiento,profesion):
        super().__init__(nombre,ci,fechaNacimiento)
        self.profesion=profesion
    def hablar(self):
        print("El docente esta hablando en lenguaje tecnico")


estudiante=Estudiante("Kevin Arroyo",7411555,"15-12-1995",44554,"Ingenieria de Sistemas")
estudiante.hablar()
docente=Docente("Juan Perez",2323030,"30-03-1990","Ingeniero de Sistemas")
docente.hablar()