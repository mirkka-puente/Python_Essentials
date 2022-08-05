# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:10:43 2022

@author: User
"""
try:
    x = int(7)
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide this by zero")
except ValueError:
    print('You must enter an integer')
    #except sin nombre en espicifico va al final
except:
    print("oh dear, something went wrong...")
print("END.")

try:
    y = 1/0
except ArithmeticError:
    print("arithmetic error")
except ZeroDivisionError:
    print('Zero division error')
print('finish')

try:
    y = 1/0
except ZeroDivisionError:
    print("zero error")
except ArithmeticError:
    print('arithmetic error')
print('finish')


