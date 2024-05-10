print("Bienvenidos a la calculadora")
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


mensaje1 = suma
print("el resultado de la operacion es")

mensaje2 = resta
print("el resultado de la operacion es")

mensaje3 = multi
print("el resultado de la operacion es")

mensaje4 = div
print("el resultado de la operacion es")

if op.lower == "suma":
    print(mensaje1)

elif op.lower == "resta":
    print(mensaje2)

elif op.lower == "multi":
    print(mensaje3)

elif op.lower == "div":
    print(mensaje4)
