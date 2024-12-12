import math

num = int(input("Escriba un número: "))

def factorial(n):
    nf = math.factorial(n)
    print(nf)

factorial(num)
# factorial(15) Se puede pasar el parametro inmediatamente
# print(factorial(15)) Se puede imprimir desde afuera si se retorna la variable "return"
# valor = factorial(20) Se puede guardar el valor en una variable si se pone un "return" en la función 
