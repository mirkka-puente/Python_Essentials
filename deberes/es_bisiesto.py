# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 18:30:13 2022

@author: User
"""

def isYearLeap(a):
    if a%4 == 0:
        if a%100 == 0 and a%400 != 0:
            return False
        else: return True
    else: return False

print(isYearLeap(1900))

testData = [1900, 2000, 2016, 1987]

testResults = [False, True, True, False]

for i in range(len(testData)):

            yr = testData[i]

            print(yr,"->",end="")

            result = isYearLeap(yr)

            if result == testResults[i]:

                        print("OK")

            else:

                        print("Failed")
                        

"""
Su tarea es escribir y probar una función que toma dos argumentos (un año y un mes) 
y devuelve el número de días para el par mes / año dado 
(aunque solo febrero es sensible al valor del año, su función debería ser universal).
La parte inicial de la función está lista. Ahora, modifique a la función para que use la opción
de return None si sus argumentos no tienen sentido.
Por supuesto, puede (y debe) usar la función previamente escrita y probada
(LAB Listas y return). Puede ser de mucha ayuda.
Lo alentamos a que use una lista con los meses. 
Puede crearlo dentro de la función: este truco acortará significativamente el código.

- Año bisiesto -> febrero tiene 29 dias
- Año normal:
    Tienen 31 días: Enero(1), marzo(3), mayo(5), julio(7), agosto(8), octubre(10) y (12)diciembre.

    Tienen 30 días: Abril(4), junio(6), septiembre(9) y noviembre(11).

    Tienen 28 días: Febrero (2).

"""

def daysInMonth(yy, mm):
    less_days = [4, 6, 9, 11]
    if mm > 12 or mm == 0:
        return None
    elif mm == 2:
        if isYearLeap(yy):
            return 29
        else: return 28
    else:
        if mm in less_days:
            return 30
        else:
            return 31

testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):

              yr = testYears[i]

              mo = testMonths[i]

              print(yr, mo, "->", end="")

              result = daysInMonth(yr, mo)

              if result == testResults[i]:

                            print("OK")

              else:

                            print("Failed")

                    
"""Su tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un 
día del mes) y devuelve los días correspondiente del año, o devuelve None si alguno de los 
argumentos es inválido.Use las funciones previamente escritas y probadas. 
Agregue algunos casos de prueba al código. Esta prueba es solo un comienzo."""

def dayOfYear(year, month, day):
    count = 0
    if month <= 12 and day <= 31:
        for m in range(1, month):
            count = count + daysInMonth(year, m)
    else:
        return None
    count = count + day
    return count
  
print('\n')          

testYY = [1900, 2000, 2016, 1987, 2022, 2021]

testMM = [12, 12, 1, 4, 1, 15]

testDD = [31, 31, 1, 25, 31, 10]

testR = [365, 366, 1, 115, 31, None]

for i in range(len(testYY)):

              y = testYY[i]

              m = testMM[i]
              
              d = testDD[i]

              print(y, m, d, "->", end="")

              r = dayOfYear(y, m, d)

              if r == testR[i]:

                            print("OK")

              else:

                            print("Failed")




                      
