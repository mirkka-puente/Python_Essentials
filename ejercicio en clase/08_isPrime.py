# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 11:31:09 2022

@author: User
"""

def isPrime(num):
    if num == 1 or num == 2:
        return True
    helper = []
    for i in range(2, num):
        if num%i == 0:
            helper.append(False)
        else:
            helper.append(True)
    return isTrue(helper)
    
def isTrue(lista):
    for l in lista:
        if l == False:
            return False
    return True


        
print(isTrue([False, False]))
print(isTrue([True, False]))
print(isTrue([True, True]))
print(isTrue([False, True, True]))

print('\n')

print(isPrime(30))
print('\n')
        
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print('\n')

x=7
y=6
res = lambda x, y: x+y
print(res(x, y))
print(res(4, 3))




        


           


