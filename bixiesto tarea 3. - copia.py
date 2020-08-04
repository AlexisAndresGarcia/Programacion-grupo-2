# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:12:54 2020

@author: Alexis Garcia
"""

def diasyFecha(año):
    if año % 4 == 0:
            return False
    elif año % 100!= 0 :
            return True
    elif año % 400!= 0:
        return False
    else:
         return True

def diasymenes(año,mes):

     if año < 1900 or mes < 1 or mes > 12:
         return 
     
        
     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     res  = days[mes - 1]
     if mes == 2 and diasyFecha(año):
	     res = 29
     return res

def diayaños(año , mes, dia):
    days=0
    for m in range(1,mes):
        md = diasymenes(año, m)
        if md == None:
            return None
        
        days += md
        
    md = diasymenes(año , mes)
    if dia >= 1 and dia <= md:
        return days + dia
    else:
        return None   
print(diayaños(2018,10,31))