# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:49:24 2020

@author: morte
"""
class Menu(object):
    def mostrarMenu(self):
        print('Menú de Opciones: ')
        print('-----------------')
        print('1 - Crear un Punto 2d')
        print('2 - Crear un Punto 3d')
        print('3 - Guardar Puntos en Archivo')
        print('4 - Leer datos de Puntos')
        print('5 - Mostrar datos Puntos')
        print('6 - Salir')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion=int(input('Seleccione un número del 1 al 6: '))
            if opcion in [1,2,3,4,5,6]:
                opcionCorrecta=True
        return opcion        
