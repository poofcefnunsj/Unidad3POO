class Paciente:
    __dni=0
    __apellido=''
    __nombre=''
    __prescripciones=[]
    def __init__(self, dni, apellido, nombre):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
    def addPrescripcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)
