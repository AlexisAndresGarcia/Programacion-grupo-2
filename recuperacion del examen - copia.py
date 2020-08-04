# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 17:07:19 2020

@author: Alexis Garcia   Grupo:2    4-08-2020
"""

print("programa:  analiza la temperatura del agua")
temperatura = []
n = int(input("Digite las temperaturas(1,10): "))
for i in range(n):
 num = int(input("agregar la temperatura en °C :"))
 temperatura.append(num)
G = 0
L = 0
S = 0
for num in temperatura:
    if (num==100 or num>100):
        G=G+1
    elif (num < 0 or num==0):
        S=S+1
    elif (num>0 or num<100):
        L= L+1
print()
print("Resumen de las muestras de agua analizadas")
print("cantidad en muestras solidad:", S)
print("cantidad en muestras liquidas:", L)
print("cantidad en muestras gaseosas:", G)
i=0
print("Ingrese la temperatura")
tt1=int(input("Temperatura 1 °C:"))
tt2=int(input("Temperatura 2 °C:"))
tt3=int(input("Temperatura 3 °C:"))
ttT =(tt1+tt2+tt3)
proC =ttT/3
e1 =(tt1 * 9/5)+32
e2 =(tt2 * 9/5)+32
e3 =(tt3 * 9/5)+32
proF = (e1 + e2 + e3) / 3
print("promedio de temperaturas en °C:", proC)
print("promedios de temperatura en °F:", proF)
