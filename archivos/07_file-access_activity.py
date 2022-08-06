# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 18:46:57 2022

@author: User
"""

#la 'a' es agregacion
file = open('devices.txt', 'a')

while True:
    x = input('Add a new item:')
    newItem = x
    file.write(newItem + '\n')
    if newItem == "exit":
        print("All done!")
    break

file.close()
    