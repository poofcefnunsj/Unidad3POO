# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:11:48 2020

@author: morte
"""

class Gobernador:
    __dni=0
    __nombreApellido=''
    __provincia = None
    def __init__(self, dni, nombreApellido, provincia=None):
        self.__dni=dni
        self.__nombreApellido=nombreApellido
        self.__provincia=provincia
        if self.__provincia != None:
           self.__provincia.setGobernador(self)
    def __str__(self):
        cadena = 'DNI: %d, Nombre y Apellido: %s' % (self.__dni, self.__nombreApellido)
        return cadena
    def setProvincia(self, provincia):
        self.__provincia=provincia