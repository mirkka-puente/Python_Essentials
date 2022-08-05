# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:11:12 2022

@author: User
"""
def mensaje():
    print(4+5)
    print("That's my name")
    
mensaje()

#fuentes de funciones: python itself, modules(librerias), 
#code (we create these ones),y con objeto directo

def saludo(name):
    print("Hola,", name)
    
saludo("Mirkka")

def saludo2(nombre1, nombre2):
    print("Hola,", nombre1, "\n"*2)
    print("Hola,", nombre2)

saludo2("Mirkka","Jossette")
saludo2("Anita","Maria")

def delivery(barrio, calle, casa):
    print("The address of your order is: ", 
          barrio, " ", 
          calle, " ", 
          casa)
    
delivery('Alangasi', "Maria Borrero", "N35B")

def resta(a, b):
    #print(a - b)
    return a - b
    
resta(a = 3, b=2)
resta(b=2, a=5)
resultado=resta(4, 6)
print(resultado)

def suma(a, b):
    return a+b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    return a/b

def exponente(a, b):
    return a**b

mi_suma=suma(4, 7)
num = multiplicacion(3, 2)
div = division(8, 2)
exp = exponente(2, 6)

def funlista(lista):
    for nombre in lista:
        print("Hola, ", nombre)
    print("\n")
    
funlista(["Ana"])
funlista(["Mirkka", "Ana"])

def crealista(n):
    lista = []
    for item in range(1, n+1):
        lista.append(n)
    print(lista)
    return lista
        
crealista(7)

##FUNCIONES LAMBDA - para funciones pequenias
# f = lambda argument:return


