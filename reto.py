# # Implementar un generador de contraseñas seguras que permite al usuario especificar la longitud de la contraseña y decidir si desea incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos. La generación de contraseñas se realiza a través de una función que toma la longitud y las preferencias del usuario y devuelve una contraseña segura. El programa ofrece un menú interactivo para probar el generador de contraseñas y permite al usuario realizar múltiples solicitudes.
# Instrucciones:
# Al inicio, el programa dará la bienvenida y proporcionará una descripción del generador de contraseñas seguras.
# Presentará un menú con opciones numeradas para que el usuario pueda elegir la longitud de la contraseña, incluir mayúsculas, minúsculas, caracteres alfanuméricos y símbolos.
# Utilizará una función para generar la contraseña según las preferencias del usuario.
# Mostrará la contraseña generada y preguntará si el usuario desea generar otra contraseña.
# Si el usuario decide salir, se despedirá y el programa se cerrará.

import random

print("Bienvenido al generador de contraseñas seguras")
print(" ")
print("El generador de contraseñas permite crear una contraseña de la logitud deseada, con la opción de incluir mayúsculas, minúsculas, carácteres alfanumericos y simbolos, asegura tus cuentas con nuestro programa.")

print(" ")
print("Menú de opciones")
print("Acontinuación, se le preguntará que opciones desea usar en su contraseña")
print(" ")
long = int(input("Ingrese la longitu de la contraseña: "))

print("1. Incluir mayúsculas")
mayus = bool(int(input("Desea incluir mayúsculas?: 1. si - 0. no ")))

print("2. Incluir minúsculas")
minus = bool(int(input("Desea incluir minúsculas?: 1. si - 0. no ")))

print("3. Incluir carácteres alfanuméricos")
calf = bool(int(input("Desea incluir carácteres alfanuméricos?: 1. si - 0. no ")))

print("4. Incluir simbolos")
simb = bool(int(input("Desea incluir simbolos?: 1. si - 0. no ")))

cont = []
mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
minusculas = ["a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
simbolos = ["!", "$", "&", "%"]

def contraseña():
    i = 0

    a = random.randint(0, 27)
    b = random.randint(0, 9)
    c = random.randint(0, 4)

    for i in long:
        if mayus:
            datomayus = mayusculas[a]
            cont.append(datomayus)
            i += 1
        elif minus:
            datosminus = minusculas[a]
            cont.append(datosminus)
            i += 1
        elif calf:
            datoscalf = numeros[b]
            cont.append(datoscalf)
            i += 1
        elif simb:
            datossimb = simbolos[c]
            cont.append(datossimb)
            i +=1
    
    print(cont)



contraseña()
