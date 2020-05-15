import os

from manejadorLibros import manejadorLibros

class Menu:
    __switcher=None
    #__libros = None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.salir
                         }
        #self.__libros = libros
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, libros):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(libros)
    def salir(self):
        print('Salir')
    def opcion1(self, libros):
        band = False
        while not band:
            id = int(input('Ingrese el id del libro: '))
            os.system('cls')
            if libros.buscarId(id) == True:
                band = True
            else:
                print('Error: el id ingresado no pertenece a ningun libro.')


    def opcion2(self, libros):
        palabra = input('Ingrese una palabra: ')
        libros.buscaPalabra(palabra)
