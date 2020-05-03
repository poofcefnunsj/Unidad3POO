# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

class Provincia:  
     __nombre=''
     __cantidadDeHabitantes=0
     __gobernador=None
     def __init__(self, nombre, cantidadDeHabitantes, gobernador=None):
         self.__nombre=nombre
         self.__cantidadDeHabitantes=cantidadDeHabitantes
         self.__gobernador=gobernador
#         if self.__gobernador != None:
#             self.__gobernador.setProvincia(self)
     def __str__(self):
         return 'Provincia: %s, habitantes %d, gobernada por: %s' %(self.__nombre, self.__cantidadDeHabitantes, self.__gobernador)
     def setGobernador(self, gobernador):
         self.__gobernador=gobernador
