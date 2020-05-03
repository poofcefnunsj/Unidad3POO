class Bebida:
    __denominacion=''
    __presentacion=''
    __precio=0.0
    def __init__(self, denominacion, presentacion, precio):
        self.__denomiancion=denominacion
        self.__presentacion=presentacion
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    def getDenominacion(self):
        return self.__denomiancion
