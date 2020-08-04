# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:00:40 2020

@author: Bryan
"""


a=int(input("ingrese su primera calificacion"))
b=int(input("ingrese su segunda calificacion"))
c=int(input("ingrese su tercera calificacion"))
if a>=c and b>=c :
    t=a+b
else:
    if a>=b and c>=b:
        t=a+c
    else :
        t=b+c
print("su calificacion total es :",t)
