# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 12:21:09 2020

@author: Alexis Garcia
"""
while True:
    x=input("Ingrese el numero:")
    if x=="q" or x=="quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
    