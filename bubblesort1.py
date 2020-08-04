# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:11:22 2020

@author: Alexis Garcia
"""
vec=[2,78,9,7,12,95,6,1,3,4];
band=int(0);
while band==0:
    band=1;
    for i in range(0,100):
        if(vec[i]>vec[i+1]):
            aux=vec[i+1];
            vec[i+1]=vec[i];
            vec[i]=aux;
            band=0;
print(vec)
    
    
