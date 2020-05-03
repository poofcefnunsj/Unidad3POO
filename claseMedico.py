class Medico:
    __dni=0
    __matricula=0
    __especialidad=''
    __apellido=''
    __nombre=''
    __prescripciones=[]
    def __init__(self, dni, matricula, especialidad, apellido, nombre):
        self.__dni=dni
        self.__matricula=matricula
        self.__especialidad=especialidad
        self.__apellido=apellido
        self.__nombre=nombre
    def addPrescipcion(self, prescripcion):
        self.__prescripciones.append(prescripcion)
