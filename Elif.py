
"""
Created on Tue Jun 23 11:17:55 2020

@author: Alexis Garcia
"""
acl= input("Ingrese ek numero de ACL") 
acl= int(acl)
print("\n"*2)
if acl >=1 and acl <=99:
    print("Este ACL standard")
elif acl >=100 and acl <=199:
    print("Es ACL extended")
else: 
    print("No es ACL")
