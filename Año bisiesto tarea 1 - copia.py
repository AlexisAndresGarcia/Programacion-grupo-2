# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 14:33:52 2020

@author: Alexis Garcia    Grupo:2    Fecha:2-7-2020
"""

def este_año_es_bisiesto(año):
    if año %400==0:
        return True
    elif año %100==0:
        return False
    elif año %4==0:
        return True
    else:
        return False

año=2020
print((este_año_es_bisiesto(año)))
 
Datos_de_prueba = [1900, 2000, 2016, 1987]
Resultados_de_prueba = [False, True, True, False]
for i in range(len(Datos_de_prueba)):
	yr = Datos_de_prueba[i]
	print(yr,"->",end="")
	resultado = este_año_es_bisiesto(yr)
	if resultado == Resultados_de_prueba[i]:
		print("OK")
	else:
		print("Failed")
