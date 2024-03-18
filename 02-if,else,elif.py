edad = input("ingrese edad")
edad = int(edad)
if edad > 65:
    print("Puede ver la pelicula con super descuento")

    print("Listo")

elif edad > 54:
    print("puede ver la pelicula con descuento")

    print("listo")

elif edad > 17:
    print("puede ver la pelicula")

    print("listo")

else:
    print("no puede ver la pelicula")

    print("listo")
# si se le da un valor a una variable y esta cumple con las condiciones del if, imprimira los mensajes siguientes, de otra manera, no imprimira nada.
# En este ejemplo se puede ver como se agrega un input y se convierte en un numero para poder ingresar el valor y verificar si cumple con la condicion del if, de otra manera
# se imprimira el mensaje de que no puede ver la pelicula.
# Es sumamente importante el orden en el que se se ponen los datos cuando se esta utilizando el "elif", ya que dependiendo de esto, el resultado que se imprimira va a variar.
# Se pueden agregar varios "elif"
