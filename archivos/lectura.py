# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 18:33:43 2022

@author: User
"""
lista=[]
#file open con nombre del archivo
#si no esta la 'r', el code asume que es de lectura igual
file = open('devices.txt', 'r')
#item en el file que estoy trabajando
for item in file:
    #elimina los saltos de linea o cualquier palabra
    item = item.strip()
    print(item)
    lista.append(item)
file.close()
    