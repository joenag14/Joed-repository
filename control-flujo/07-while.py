numero = 1
while numero < 100:
    print(numero)
    numero *= 2
else:
    print("se alcanzo el limite")


# En el ejemplo anterior se hace uso de un while, multiplicando el numero 1 declarado en la variable numero* 2
# y va a seguir mostrando el numero mientras (while) este menor que 100.
# En este caso, tambien se puede visualizar como hacer el uso de un while else, agregando un mensaje como
# "se alcanzo el limite", de esta manera, se puede terminar dar un mensaje de terminacion al while.

comando = ""
while comando != "salir":
    comando = input("$")
    print(comando)

    # esta es una manera de agregar un input al while en el cual el loop continuara mientras que la palabra o numero
    # ingresado en el while no se ingrese, el sistema mantendra repitiendo el loop interminablemente.

comando = ""
while comando.lower != "salir":
    comando = input("$")
    print(comando)

# En este ejemplo le agregamos la funcion de .lower, no importara la manera en la que se escriba salir,
# el sistema terminara el loop.

comando = ""
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break

# En este caso, se realizo un loop infinito al tener un "while true", es importante que SIEMPRE
# que agreguemos un loop infinito, le agreguemos a este una condicion de salida, en este caso el "break".
