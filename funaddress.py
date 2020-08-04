# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 11:38:45 2020

@author: Alexis Garcia
"""
def direccion(calle,sector,codigopostal,referencia,numcasa):
    print("Su direccion es;","Su sector es;",sector,"Calle",calle)
    print("Su casa es la #;",numcasa,"Con codigo postal#;",codigopostal)
    print("y está cerca de;",referencia)
    
print("Ingrese los datos que se solicitaan de su direccion") 
c=input("Ingrese la calle:")
s=input("Ingrese sector de residencia:")
cod=input("Ingrese codigo postal:")
r=input("Ingrese una referencia de su domicilio:")
num=input("Ingrese el # de casa:")

direccion(c,s,cod,r,num)
