# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:18:24 2020

@author: Alexis Garcia     Grupo: 2  Fecha:24-07-2020
"""

import numpy as np

from random import randint

print("\nIngrese la cantidad de filas que se nesecitan: ")
filas=int(input())   
 
print("\nIngrese la cantidad de columnas que se nesecitan: ")
columnas=int(input())

print("\n"*0)

matrix=np.zeros([filas,columnas])
d=-1
x=-1
w=filas
q=filas

for i in range(0,filas):
    for n in range(0,columnas):
        matrix[i][n]=int(randint(0,99))
        
print("<< La matriz es de",filas,"x",columnas,">>")
print("\n"*0)
print(matrix)
print("\n"*0)

print('la diagonal principal de la matriz es: ')
print("\n"*0)

for j in range(0,filas):
    if d<filas:
        d+=1
        w-=1
        
    print(' | -- |'*d,"|",int(matrix[j][d]),"|",'| 0 | '*w)
    
print('\nla diagonal secundaria de la matriz es: ')
print("\n"*0)

for k in range(0,filas):
    if x<filas:
        x+=1
        q-=1
        
    print(' | -- |'*q,"|",int(matrix[k][q]),"|",'| 0 | '*x)

