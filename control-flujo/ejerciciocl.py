print("Bienvenido a las calculadora")
print("Para salir, escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado=""

while True:
    if not resultado: 
        resultado= input ("Ingrese numero:")
        if resultado.lower()== "salir":
            break
        resultado= int(resultado)
    op  = input("ingresa operacion:")
    if op.lower( ) == "salir":
        break
    n2= input("ingrese siguiente numero: ")
    if n2.lower()== "salir":
        break
    n2= int(n2)

    if op.lower()== "suma":
        resultado += n2
    elif op.lower()== "resta":
            resultado -= n2
    elif op.lower()== "multi":
            resultado *= n2
    elif op.lower()== "div":
            resultado /= n2
    else:
         print("Operacion no valida")
         break
    
    print(f"El resultado es {resultado}")