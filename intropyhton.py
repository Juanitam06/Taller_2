#comentario de una linea
#todo lo que va despues es ignorado por el interprete de python

#Variables: Espacio de memoria, con nombre, donde guardo valores
#los nombres de variables deben ser cortos, descriptivos, NO TENER ESPACIOS
#EN BLANCO ni caracteres especiales, ni numeros

#Descriptivo significa que representa la categoria del dato que quiero guardar
#En python las variables pueden contener cualquier dato de tipo primitivo
#D.P: numeros enteros o reales, cadena de caracteres (string), boleanos (True, FALSE), caracteres

variable= 1 

variable= 'Cadena de texto'

variable= True

variable= 'a'

variable= 3.1415926535

# Para asignar un valor a la variable se usa el operador = 

#Operadores: Mecanismo para obtener un dato a partir de otros datos
#Los datos que intervienen se llaman operandos.

#Aritmeticos: + - * / %
#Comparacion: retorna True or False. <> <= >= == !=
#Logica booleana: OR AND, retornan TRUE OR FALSE de acuerdo a la tabla de verdad
#Los operandos siempre son booleanos (True or False)

a= True
b= False

print(a and b)

#Los operadores booleanos y de comparacion son muy utilizados al definir condiciones

# Estructuras de control de codigo/FLUJO : En general un programa se ejecuta
#linea por linea de manera secuencial. Se puede romper esa secuencialidad
#empleando un conjunto de secuencias o expresiones que permite:
# 1. Seleccionae la ejecucion de un bloque de codigo
# 2. Repetir la ejecucion de un bloque de codigo
# 3. Seleccionar entre ejecutar un bloque de codigo u otro bloque de codigo
#De esa manera podemos "Romper" la secuencialidad
#Principios del paradigma de programacion estructurado

#Sentencia if. Si se cumple una condicion (se evalua como True)
# se ejecuta un bloque de codigo

print("Linea 1")
print("Linea 2")
if 5>3:
    print("Esto se muestra si la condicion es verdadera")

#3.

if 5>8 or 3<7:
    print("Esto se muestra si la condicion es verdadera")
else:
    print("Esto se muestra si la condicion es falsa")
    
#Otro ejemplo

entrada= int(input("Cuantos años tiene?"))

if entrada<18:
    print("Es un menor de edad.")
else:
    print("Ya esta grande...")