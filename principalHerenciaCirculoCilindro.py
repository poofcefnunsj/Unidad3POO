# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 00:36:02 2020
@author: morte
"""
from claseCirculo import Circulo
from claseCilindro import Cilindro
def testCirculoCilindro():
    circulo = Circulo(3)
    cilindro = Cilindro(5,7)
    circulo.listar()
    cilindro.listar()
if __name__=='__main__':
    
    testCirculoCilindro()
