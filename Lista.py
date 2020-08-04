
"""
Created on Tue Jun 16 12:32:30 2020

@author:Alexis Garcia
"""

hostnames=["R1","R2","R3","S1","S2","S3"]
print(type(hostnames))
print(len(hostnames))
print(hostnames)
print(hostnames[0])
print(hostnames[1])
print(hostnames[2])
print(hostnames[3])
print(hostnames[4])
print(hostnames[5])
print(hostnames[-1])
print(hostnames[-2])
hostnames[5]="S4"
hostnames[5]="S5"
del hostnames[0]
