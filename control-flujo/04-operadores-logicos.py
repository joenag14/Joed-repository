# and, or, not.


gas = True
encendido = True


if gas and encendido:
    print("puedes avanzar")

    # para que el resultado de and sea "True" ambas variables deben ser "True", de otra manera el resultado sera "False"
    # En el caso del or, con que alguno de los dos sea True, eso sera suficiente para que el resultado sea True, si ambos resultados son False, no arrojara el resultado o
    # imprimira en este caso el "puedes avanzar".

gas = True
encendido = False

if gas or encendido:
    print("puedes avanzar")

    # El not se debe poner antes de la variable a editar y lo que hara es cambiar el resultado por ejemplo si esta false, se pasara a true y viceversa, como se puede evidenciar.
    # a continuacion.

gas = False
encendido = False

if not gas or encendido:
    print("puedes avanzar")

gas = True
encendido = True
edad = 18

if gas and encendido and edad > 17:
    print("puedes avanzar")

# de esta manera se puede hacer un if con tres variables diferentes.
