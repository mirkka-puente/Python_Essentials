# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 21:29:46 2022

@author: User
"""
def fibo(n):
    n1 = 0
    n2 = 1
    acc = 0
    if n == 0:
        print(n1)
    elif n == 1:
        print(n1, n2)
    else:
        while acc < n-1:  
            print(n1)
            f = n1 + n2 
            n1 = n2
            n2 = f 
            acc+=1
            
#print(fibonacci(8))