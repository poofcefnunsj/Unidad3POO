# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:38:14 2020

@author: morte
"""
#Opciones del menu

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.unionConjuntos,
                            2:self.diferenciaConjuntos,
                            3:self.igualdadConjuntos,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def salir(self):
        print('Salir')
    def unionConjuntos(self):
        print('Unión')
    def diferenciaConjuntos(self):
        print('Diferencia')
    def igualdadConjuntos(self):
        print('Igualdad')

if __name__ == '__main__':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Union de dos conjuntos
              2 Diferencia de dos conjuntos
              3 Igualdad entre dos conjuntos""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0
