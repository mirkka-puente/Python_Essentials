# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 19:10:44 2022

@author: User
"""
def readint(prompt, min, max):
    try:
        print(prompt)
        x = input()
        if (x < min) or (x > max):
            print("The number is:", x)
        else:
            print("Error: el valor no está en el rango permitido",'(', min, max,')')
            print(prompt)
    except ValueError:
        print("Error: Error en el ingreso ")
        print(prompt)
        