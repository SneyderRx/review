# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

v = int(input("Ingrese el valor a pagar: "))
i = int(input("Ingrese el IVA a aplicar: "))

def factura():
    iva = v * (i / 100)
    iva21 = v * 0.21

    fac = v + iva if i else v + iva21 # Evaluo si "i" tiene valor, lo que retornaría "True" o si es "0" retornará "False".
    
    print(f"El total de su factura es: {fac}")

factura()