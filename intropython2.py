#while
#while <condicion verdadera>
#     cuerpo del ciclo
#Condiciones son: expresiones booleanas (or,and) y operaciones de comparacion
#cicclos controlados por un controlador entero

i=0

while i<10:
    print("ciclo")
    #importante modificar el valor del contador
    i=i+1 o i+=1
     
while 1==1
    print("ciclo")
    
#ciclos controlados por el valor de una variable

import random
a=0

while a!= 5:
    a= random.randint(1,10)
    print (a)
    
print ("Se acabo")

#ciclos controlados por un evento

a=0
while 1==1:
    
    a=int(input("Ingrese un numero"))
    if a==10:
        break
    

#Lista: Conjunto de variables organizadas en espacios consecutivos
#de memoria. A las que se les asigna un unico nombre, se diferencian por la posicion 
#que ocupan respecto al primer elemento de la lista

miLista= [1, True, "Textos", 3.89]
miLista2= []  #lista vacia

#En python todos son objetos.

miLista.append #agrega un elemento al final de la lista
miLista.insert #inserta un objeto antes del indice indicado
miLista.pop #remueve el item en el indice que se le indique


#Tupla: lista inmutable
miTupla=()

# for: se utiliza para recorrer un "iterables". El cuerpo
#se repite tantas veces como elementos tenga el iterable, en cada ciclo
# se

#Estructura del for en python:
# for variable_donde_guardo_el_elemento in iterable:

miLista = [5,45,89,6,7]

for x in miLista:
    print(x)             #Esto imprimiria 5, puesto que es la variable guardada en x
    break                # y luego se detiene por el break

for x in miLista:
    if x>50                #Imprime solo una vez "Grande" porque en la lista solo hay un
    print ("Grande")       # numero mayor a 50 en la lista
    
#si solo utilizo el iterable para definir la cantidad
#de repeticiiones entonces no es necesaria la variable

for _ in miLista:
    print ("Ciclo")
    
#Si no tengo un iterable puedo usar la funcion range()
#para generar una secuencia de numeros

for x in range (-10, 10):
    print(x)               
    
#Taller: crear un programa que pida un numero al usuario y:
#1. Imprima los numeros impares entre -numero y numero
#2. Imprima los numeros primos entre 0 y numero*100
#El programa debe garantizar que el usuaruio ingrese un numero>0