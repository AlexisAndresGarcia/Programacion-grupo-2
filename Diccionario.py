# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:12:41 2020

@author: Alexis Garcia
"""

ipadd={"R1":"10.0.0.1","R2":"10.0.0.2",
       "R3":"10.0.0.3","S1":"10.1.0.1",
       "S2":"10.1.0.2"}
print(type(ipadd))

dict1={"usuario1":"1725661696","valor":5000,"edad":18,"casado":False, "RATE en %":52.2} 
print(ipadd["R1"])
ipadd["S3"]="10.1.0.4"
print("S1"in ipadd)
print("edad" in dict1)
