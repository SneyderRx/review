import math

#num = int(input("Escriba un número: "))

def factorial(n, m): #Si se usan dos parámetros en la función, para ingresar se necesitan dos parámetros.
    nf = math.factorial(n)
    mf = math.sqrt(m)
    print(nf)
    print(mf)

#factorial(num) No ingresará a la función porque se neceitan dos parámetros.
factorial(5, 30)
# factorial(15) Se puede pasar el parametro inmediatamente
# print(factorial(15)) Se puede imprimir desde afuera si se retorna la variable "return"
# valor = factorial(20) Se puede guardar el valor en una variable si se pone un "return" en la función 
