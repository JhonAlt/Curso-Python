## Listas ##

my_list = list()# Las listas se pueden definir con paréntesis.
my_other_list = []# También se pueden utilizar corchetes.

print(len(my_list))

my_list = [30, 24, 43, 60, 56, 17, 30]# Se pueden agregar elementos a la lista separándoles por comas.

print(my_list)
print(len(my_list))

my_other_list = [27, 1.65, 'Jonathan', 'Amézquita']# Se pueden agregar distintos tipos de datos a una lista

print(type(my_list))
print(type(my_other_list))

# Podemos mostrar los diferentes elementos de la lista por medio del indice individual de cada uno
# En este caso se pide que se muestre el elemento del indice cero de la lista a la consola "[0]" que seria el "27"
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
# Se pueden mostrar indices negativos siempre y cuando coincidan con la cantidad de elementos dentro de la lista.
# De sobrepasar ese limite, se muestra un mensaje de error.
#print(my_other_list[-5])# IndexError
#print(my_other_list[4])# IndexError

print(my_list.count(30))# 'count' cuenta cuantas veces se repite un elemento dentro de la lista.
print(my_other_list.count('Jonathan'))

age, height, name, surname = my_other_list
print(surname)
# También se pueden definir como variables los elementos dentro de la lista.

print(my_list + my_other_list) #Se pueden concatenar listas
#print(my_list - my_other_list) ERROR

my_other_list.append('FlexCel') # Añade un nuevo elemento al final de la lista.
print(my_other_list)

my_other_list.insert(1, 'Negro') # Se añade un nuevo elemento a la lista dentro del indice especificado.
print(my_other_list)

my_other_list.remove('Negro')# Elimina un elemento que sabemos que existe dentro de la lista.
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())## pop elimina el ultimo elemento de la lista y retorna el valor eliminado.
print(my_list)

my_pop_element = my_list.pop(2)## El valor eliminado se puede almacenar en una variable.
print(my_pop_element)
print(my_list)

del my_list[2]# Se elimina un elemento especificado por indice dentro de la lista.
print(my_list)

my_new_list = my_list.copy ## Se realiza una copia exacta de la lista

my_list.clear()# Elimina todos los elementos dentro de la lista.
print(my_list)
print(my_new_list)


my_list = 'Hola Python' #Python es de tipado dinámico por lo que se puede reasignar otro dato a la lista
print(my_list)
print(type(my_list))