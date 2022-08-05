# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:11:15 2022

@author: User
"""

#for item in range(2, 10, 2):
    #print(item)
    
lista = ["R1", 'R2', 'R3', 'R4', 'S1', 'S2', 'S3']   
l2 = ['mirkka', 'camila', 'carlitos']
l3 = []
lista2 = []

for i in lista:
    if 'R' in i:
        l3.append(i)

print(l3)     

for i in lista:
    if 'R' not in i:
        lista2.append(i)
               
        
print(lista2)

result = 0
n = 6
for i in range(1, n+1, ++1):
    print(i)
    result += i
print(result)
    
print('el resultado de la suma de 1 hasta n, es:', result)    


#while se va a correr mientras sea verdad
#contar = input('Ingrese el # al que debo contar: ')

contar = 10
contador = 1

while contador <= contar:
    print(contador)
    contador += 1
   
while True:
    print(contador, end = ' ')
    contador +=1
    if contador > contar:
        break
    
print('\n')

x = "q"
while True:
    print("mirkka")
    if x=='q' or x=='quit':
        break
    x = 3
    y = 1       
    while True:
        print(y)
        y +=1
        if y > x:
            break
    
    
    
    