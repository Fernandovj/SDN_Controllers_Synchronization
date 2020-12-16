import numpy as np 

def average(lista): # funcion para retornar el promedio de una lista de datos
    sum=0.0
    for l in range(0,len(lista)):
        sum=sum+lista[l] 
    return sum/len(lista)



