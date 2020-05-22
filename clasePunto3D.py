# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:41:00 2020

@author: morte
"""
from clasePunto2D import Punto2D
class Punto3D(Punto2D):
    __z=0
    def __init__(self, x, y, z):
        super().__init__(x,y)
        self.__z=z
    def __str__(self):
        cadena='(x,y,z)=({}, {}, {})'.format(self.getX(), self.getY(), self.__z)
        return cadena
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                                    x=self.getX(),
                                    y=self.getY(),
                                    z=self.__z
            )
        )
        return d