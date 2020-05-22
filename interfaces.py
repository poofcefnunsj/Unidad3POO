# -*- coding: utf-8 -*-
"""
Created on Fri May 22 00:05:25 2020

@author: morte
"""
from zope.interface import Interface
'''Declaración de interface ICajero
   El Cajero solo puede buscar productos por descripción
   el método declarado es
   buscarProductoPorDescripcion(descripcion)
   '''
class ICajero(Interface):
    def buscarProductoPorDescripcion(descripcion):
        pass
'''Declaración de interface ISupervisor
   El Supervisor modificar el precio de un producto, que busca por código
   Los métodos que declara la intereface es
   buscarProductoPorCodigo(codigo)
   modificarPrecioProducto(codigo, precio)
   '''
class ISupervisor(Interface):
    def buscarProductoPorCodigo(codigo):
        pass
    def modificarPrecioProducto(codigo, precio):
        pass
