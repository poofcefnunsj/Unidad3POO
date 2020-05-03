# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:13:09 2020

@author: morte
"""
from claseProvincia import Provincia
from claseGobernador import Gobernador
def testAsociacion():
    provincia = Provincia('San Juan',681055)
    gobernador = Gobernador(27888111, 'Sergui Uñac', provincia)
    provincia.setGobernador(gobernador)    
    print(provincia)    
if __name__=='__main__':
    testAsociacion()