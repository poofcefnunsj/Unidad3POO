# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:24:29 2020

@author: morte
"""
class Nodo:
    __profesor=None
    __siguiente=None
    def __init__(self, profesor):
        self.__profesor=profesor
        self.__siguiente=None
    def setSiguiente(self, siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def getDato(self):
        return self.__profesor