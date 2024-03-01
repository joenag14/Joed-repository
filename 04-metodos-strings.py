animal = "  chanCHito feliz  "
print(animal.upper()) # Vuelve todas las letras del string mayusculas.
print(animal.lower()) # Vuelve todas las letras del string minusculas.
print(animal.strip().capitalize()) # vuelve mayuscula la primera letra del string, en este caso, se agrego
#un stip antes para eliminar los espacios antes de las letras y poder hacer la primera letra mayuscula. 
print(animal.title()) # vuelve la primera letra de cada palabra mayuscula. 
print(animal.strip()) #elimina los espacios antes y despues del texto en un string. 
print(animal.lstrip())# L "left" elimina los espacios en la izquierda
print(animal.rstrip()) # r "Right" elimina los espacios de la derecha en el string.
print(animal.find("CH")) # Ubica el indice (numero) en el que se encuentra ubicado la letra o letras que 
# se estan buscando dentro del string.
print(animal.find("cH")) # si se busca algun caracter que no este en el string el resultado 
#va a ser un numero negativo
print(animal.replace("nCH", "j"))# reemplaza las letras que estan entre las comillas  de la izquierda por 
#la o las de la derecha
print("nCH" in animal) # nos confirma por medio de un dato boolean (true) si los caracteres buscados 
# estan en el string que se esta buscando, de lo contrario, el resultado sera (false).
print( "nCH" not in animal)# nos confirma por medio de un dato boolean (false) en caso de estar 
#si los caracteres buscados estan en el string que se esta buscando, en caso de no estar el resultado sera (true).