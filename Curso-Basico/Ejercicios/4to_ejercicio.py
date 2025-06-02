## 1. Crea una lista con los números del 1 al 5 e imprímela.
lista1 = [1, 2, 3, 4, 5,]
print(lista1)

## 2. Accede e imprime el tercer elemento de la lista [10, 20, 30, 40, 50].
lista2 = [10, 20, 30, 40, 50]
print(lista2[2])

## 3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
lista1.append(6)
print(lista1)
lista1.pop()

## 4. Inserta el número 15 en la posición 2 de la lista [10, 20, 30, 40, 50].
lista2.insert(2, 15)
print(lista2)

## 5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 40, 50].
lista3 = [10, 20, 30, 30, 40, 50]
del lista3[2]
print(lista3)

## 6. Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable. Imprime la variable y la lista.
variable_pop = lista1.pop()
print(variable_pop)
print(lista1)

##7. Invierte la lista [100, 200, 300, 400, 500] e imprímela.
lista4 = [100, 200, 300, 400, 500]
lista4.reverse()
print(lista4)

## 8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
lista5 = [3, 1, 4, 2, 5]
lista5.sort()
print(lista5)

## 9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
primera_Lista = [1, 2, 3]
segunda_Lista = [4, 5, 6]
tercera_lista = primera_Lista + segunda_Lista
print(tercera_lista)

## 10. Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
sub_lista = lista3[1:3]
print(sub_lista)
print(lista3)