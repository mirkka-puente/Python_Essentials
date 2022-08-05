# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:45:41 2022

@author: User
"""
#always: try and except

try:
    print('1')
    x = 1/0
    print('2')
    #sin exception corre hasta aqui
except:
    #continua con codigo
    print('Hay un error...')
    print("3")

#sin try and except    
print('1')
x = 1/0
print('2')
print('Hay un error...')
print("3")
 
 