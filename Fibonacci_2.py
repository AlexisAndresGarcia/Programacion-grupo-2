# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:26:49 2020

@author: Alexis Garcia
"""


def fib(n):
    a=0
    b=1
    
    for k in range (n):
        c=a+b
        a=b
        b=c
    return b
for x in range(8):
    print(fib(x))