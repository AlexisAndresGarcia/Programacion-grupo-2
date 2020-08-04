# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:01:23 2020

@author: Alexis Garcia
"""
dato=input("Ingrese el numero de veces que contare:")
dato=int(dato)
contador=1
acumulador=0
while contador <=dato:
    print(contador,end=" ")
    acumulador+=contador
    contador+=1
print("\n"*2)
print("la suma de los # es: ",acumulador)
print("El promedio total es: ",(acumulador/dato))

