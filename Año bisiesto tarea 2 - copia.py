# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 15:48:02 2020

@author: Alexis Garcia    Grupo:2    Fecha:2-7-2020
"""

from calendar import monthrange
try:
    def cantidad_de_dias(mes,año):
            return monthrange (año,mes)[1]

    print(cantidad_de_dias(13,2020))
except:
    print("Error ingrese un valor valido")