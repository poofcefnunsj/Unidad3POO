# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 09:29:19 2020
@author: morte
"""
from claseAyudante import Ayudante
def testHerenciaMultiple():
    print('MRO de la clase Ayudante: ',Ayudante.mro())
    ayudante = Ayudante(41223444, 'Juarez', 'Roberto', '10/03/2020',9.65, 'LSI', 3211, 90,'POO',2500,'Sobresaliente',5)
    ayudante.mostrarDatos()
if __name__=='__main__':
    testHerenciaMultiple() 
