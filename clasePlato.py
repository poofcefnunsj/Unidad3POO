class Plato:
    __descripcion=''
    __precio=0.0
    def __init__(self, descripcion, precio):
        self.__descripcion=descripcion
        self.__precio=precio
    def getPrecio(self):
        return self.__precio
    def getDescripcion(self):
        return self.__descripcion
