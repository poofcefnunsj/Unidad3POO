# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:57:39 2020
@author: morte
"""
from clasePaciente import Paciente
from claseMedico import Medico
from clasePrescripcion import Prescripcion
def testClaseModelaAsociacion():
    paciente = Paciente(14555699, 'Vergara', 'Andrea')
    medico = Medico(19327881, 1125, 'Clínica Médica', 'González', 'Jorge')
    prescripcion = Prescripcion('11/01/2020', 'Rinitis', 'Hexaler', '10 comprimidos', '1 por día',medico, paciente)
    prescripcion2 = Prescripcion('29/01/2020', 'Otitis', 'Ciriax Gotas', 'envase 10 ml', '2 gotas cada 8h',medico, paciente)
if __name__=='__main__':
    testClaseModelaAsociacion()
