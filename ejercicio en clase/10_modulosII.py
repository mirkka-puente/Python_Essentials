# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:02:20 2022

@author: User
"""
#Alias 
#Importar un modulo con palabra clave "as"
#nombre de modulo ya no esta disponible para llamar funciones
#mi funcion de modulo debe tomar el alias "m.pi"
import math as m
import pandas as pd
import numpy as np

#en funciones tambien
from math import pi as p, sin as s
pi = 3.1416
print(pi)
print(p)
print(s(4))