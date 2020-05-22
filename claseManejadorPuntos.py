# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:45:46 2020

@author: morte
"""
class Manejador(object):
    __puntos=[]
    def __init__(self):
        self.__puntos=[]
    def agregarPunto(self, unPunto):
        self.__puntos.append(unPunto)
    def mostrarDatos(self):
        for i in range(len(self.__puntos)):
            print(self.__puntos[i])
    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                puntos=[punto.toJSON() for punto in self.__puntos]
                )
        return d