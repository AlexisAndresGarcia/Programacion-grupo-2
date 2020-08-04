# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:06:28 2020

@author: Alexis Garcia    Grupo:9  Fecha: 20-07-2020
"""

from random import randint

from time import sleep

pregunta=True
tes = int()
nombre=str()
listado=[int()for ind0 in range(100)]
while pregunta:
    
    print("\n Para que la ejecucion de acabe digite <<0>> de lo contrario puede")
    print("digite el vector, no olvides que el vector deber ser mayor que 3 y",
          "menor que 30: ")  
    
    tamaño=int(input())
    if tamaño>=3 and tamaño<=30:
        
        while pregunta: 
            
            print("[para cambiar el tamaño del vector digite <<0>> caso elija las otras opciones]")
            print("quieres trabajar con números o con caracteres. Si es con (caracteres digite <<1>>)  (números digite <<2>>): ")
            pregu=int(input())
            if pregu==1 :
                
                for i in range(1,tamaño+1):
                    
                    print("\nAgregar el nombre del estudiante",i) 
                    nombre=input()
                    listado[i-1]=nombre
                    print("En la posicion el valor es ",i," es  ", listado[i-1])
                for j in range(1,tamaño+1):
                    for l in range(1,tamaño):
                        if listado[l-1]>listado[l]:
                            tes = listado[l-1]
                            listado[l-1]=listado[l]
                            listado[l]=tes
                for k in range(1,tamaño+1):
                    print("\n"*0)
                    print("El vector ordenado en la posicion ",k," es ",listado[k-1])
            elif pregu==0:
                
                break
            else:
                
                
                for i in range(1,tamaño+1):
                    
                    listado[i-1]=randint(0,99)
                    print("\n"*0)
                    print("El valor en la posicion ",i," es  ", listado[i-1]) 
                    sleep(1)
                sleep(1)
                while pregunta:
                    
                    print("\n[Si usted quiere regresar para trabajar con números o caracteres digite <<0>> caso contrario elija",
                          "las otras opciones]")
                    print("Desea ordenar de (menor a mayor digite <<1>>) o quiere de (mayor a menor digite <<2>>): ")
                    pre=int(input())
                    if pre == 1:
                        
                        for j in range(1,tamaño+1):
                            
                            for l in range(1,tamaño):
                                
                                if listado[l-1]>listado[l]:
                                    
                                    tes = listado[l-1]
                                    listado[l-1]=listado[l]
                                    listado[l]=tes
                        for k in range(1,tamaño+1):
                            print("\n"*0)
                            print("El vector ordenado en la posicion ",k," es ",listado[k-1])
                    elif pre==0:
                        
                        break
                    else:
                        
                        for j in range(1,tamaño+1):
                            
                            for l in range(1,tamaño):
                                
                                if listado[l-1]<listado[l]:
                                    
                                    tes = listado[l-1]
                                    listado[l-1]=listado[l]
                                    listado[l]=tes
                        for k in range(1,tamaño+1):
                            
                            print("\n"*0)
                            print("El vector ordenado en la posicion ",k," es ",listado[k-1])
                            
    elif tamaño>30:
        
        print("<<El numero ingresado no cumple con la condicion de que sea esa mayor a 30,",
              "porfavor ingrese otro número>>")
    elif tamaño== 0:
        
        preguntar = False
    
    else:
        
        print("<<El numero ingresado no cumple con la condicion de que sea menor a 3,",
              "porfavo ingrese otro número>>")

