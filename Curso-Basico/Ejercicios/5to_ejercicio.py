#1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple)

#2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) y muéstralo.
segundaT_2 = (100, 200, 300, 400, 500)
print(segundaT_2[2])

#3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y observa el resultado.
#terceraT_3 = (1, 2, 3)
#terceraT_3[1] = 10

#4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 2, 3, 3, 4, 5, 3).
cuartaT_4 = (1, 2, 3, 3, 4, 5, 3)
print(cuartaT_4.count(3))

#5. Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript", "Python").
quintaT_5 = ("Java", "Python", "JavaScript", "Python")
print(quintaT_5.index('Python'))

#6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
sexta_Tup = (1, 2, 3)
septima_Tup = (4, 5, 6)
print(sexta_Tup + septima_Tup)

#7. Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).
octava_Tup = (10, 20, 30, 40, 50)
print(octava_Tup[2:4])

#8. Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante. 
novena_Tup = ("rojo", "verde", "azul")
novena_Tup = list(novena_Tup)
novena_Tup[1] = 'Amarillo'

novena_Tup = tuple(novena_Tup)
print(novena_Tup)
print(type(novena_Tup))

#9. Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
del my_tuple
#print(my_tuple)

#10. Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
decima_Tup = (100,) # para crear una tupla de un solo elemento, debes incluir una coma después del elemento, incluso si solo hay un valor
print(type(decima_Tup))
print(decima_Tup)