# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 08:54:05 2020
@author: morte
"""
from claseBebida import Bebida
from clasePlato import Plato
from clasePedido import Pedido
from claseMozo import Mozo
def testAgregacion():
    bebida = Bebida('Coca cola','1/2 litro',150)
    bebida1 = Bebida('Aquarius', '1/2 litro',100)
    plato = Plato('Lomo especial',325)
    papas = Plato('Papa frita chica',125)
    pizza = Plato('Pizza especial', 390)
    mozo1 = Mozo(1, 'López', 'Carlos')
    pedido1 = Pedido(1, mozo1, bebida, plato)
    pedido1.addBebida(bebida1,2)
    pedido1.addPlato(papas,1)
    pedido1.addPlato(plato,3)
    pedido1.cerrarPedido()
    del pedido1
    pedido2 = Pedido(2, mozo1, bebida1, papas)
    pedido2.addBebida(bebida,2)
    pedido2.addPlato(pizza,1)
    pedido2.cerrarPedido()
    
if __name__=='__main__':
    testAgregacion()
