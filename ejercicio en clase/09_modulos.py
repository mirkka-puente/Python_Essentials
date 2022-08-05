# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:12:11 2022

@author: User
"""
#import moduloName
#importar todo
import math
#namespace = son funciones definidas en los modulos
#funciones definidas en modulos no interfieren con 
#funciones que creamos en este file
pi = 3.1416
def sin():
    return 0.99999

print(pi)
print(sin())
print(math.pi)
print(math.sin(math.pi/2))

#importacion selectiva
from math import pi, sin #funcion que me interesa en math es pi y sin

#import all the functions (agresiva)
#si uso el "from" ya no uso math.func()
from math import *

