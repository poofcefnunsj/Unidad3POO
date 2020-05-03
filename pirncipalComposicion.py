# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 16:35:08 2020
@author: morte
"""
from claseProfesor import Profesor
def testComposicion():
    profesor = Profesor(11334441, 'Rodríguez', 'Myriam')
    print(profesor)
    del profesor
if __name__=='__main__':
    testComposicion()
