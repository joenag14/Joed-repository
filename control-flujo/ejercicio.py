print("♥ Bienvenidos a la calculadora ♥")
print("para salir escribe salir")
print("las operaciones son: suma, multi, div y resta")
n1 = input("ingrese primer numero:")
n2 = input("ingrese el segundo numero:")
op = input("ingrese operacion:")
n1 = int(n1)
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

if op == suma:
    print("el resultado de la operacion es")
    print(suma)


elif op == resta:
    print("el resultado de la operacion es")
    print(resta)

elif op == multi:
    print("el resultado de la operacion es")
    print(multi)

elif op == div:
    print("el resultado de la operacion es")
    print(div)

resultado= 