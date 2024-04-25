for numero in range(5):
    print(numero, numero * "hola mundo")

    # Esta es la forma basica de como funciona el for en python, y como multiplicarlo por un string.


buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break

    # Esta opcion se utiliza para buscar utilizando for, se agrega un nuevo print para saber las veces que se esta buscando o iterando el for, y se utiliza la funcion break
    # para que una vez encuentre el dato buscado, se deje de ejecutar el codigo.


buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
    else: