# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:52:06 2020

@author: Alexis Garcia
"""

def diasyFecha(dia1, mes1, año1, dia2, mes2, año2):
    
     def Bisiesto(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
     if (año1<año2):
        if Bisiesto(año1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
        restoMes = diasMes[mes1] - dia1
    
        restoYear = 0
        i = mes1 + 1
    
        while i <= 12:
            restoYear = restoYear + diasMes[i]
            i = i + 1
    
        primerYear = restoMes + restoYear
        sumYear = año1 + 1
        totalDias = 0
    
        while (sumYear<año2):
            if Bisiesto(sumYear) == False:
                totalDias = totalDias + 365
                sumYear = sumYear + 1
            else:
                totalDias = totalDias + 366
                sumYear = sumYear + 1
    
        if Bisiesto(año2) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        llevaYear = 0
        lastYear = 0
        i = 1
    
        while i < mes2:
            llevaYear = llevaYear + diasMes[i]
            i = i + 1
    
        lastYear = dia2 + llevaYear
    
        return totalDias + primerYear + lastYear  
     else:
        
        if Bisiesto(año1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        llevaYear = 0
        total = 0
        i = mes1
        
        if i < mes2:
            while i < mes2:
                llevaYear = llevaYear + diasMes[i]
                i = i + 1
            total = dia2 + llevaYear - 1
            return total 
        else:
            total = dia2 - dia1
            return total
print(diasyFecha(1, 2, 1999, 1, 12, 2001))