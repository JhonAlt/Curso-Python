my_tuple = tuple() # Las tuplas se definen con el nombre 'Tuple' o solamente con paréntesis.
my_other_tuple = ()

my_tuple = (27, 1.65, 'Jonathan', 'Amézquita', 'Jonathan')
my_other_tuple = (35, 60, 30)

print(type(my_tuple))

print(my_tuple[0])# Al igual que con las listas se puede acceder a los elementos dentro de ellas por medio de los indices.
print(my_tuple[-1])
#print(my_tuple[4]) IndexError # Cualquier indice que este fuera de rango dará un error.
#print(my_tuple[-6]) IndexError

print(my_tuple.count('Jonathan')) # Se puede contar cuantas veces aparece un valor dentro de la tupla.
print(my_tuple.index('Amézquita'))# Se puede consultar cual es el indice de un valor en especifico dentro de la tupla.

#my_tuple[1] = 1.75 #  Una tupla es inmutable, por lo que no podemos modificarla o cambiar sus elementos de forma externa.

my_sum_tuple = my_tuple + my_other_tuple # No pueden modificarse pero si pueden concatenarse entre ellas.  
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # Se muestran los elementos desde el indice 3 hasta el indice 5, ya que el 6 se excluye.

my_tuple = list(my_tuple) # Para poder volver mutable una tupla se debe transformar en una lista primero.
print(type(my_tuple))

my_tuple[4] = 'FlexCel'
my_tuple.insert(1, 'Amarillo')
print(my_tuple) # De esta manera se pueden modificar los elementos de la tupla ya que ahora es una lista normal.

my_tuple = tuple(my_tuple) # Puede volver a reasignarse como una tupla para que los elementos vuelvan a ser inmutables.
print(my_tuple)
print(type(my_tuple))

#del my_tuple # Elimina la tupla por completo.
#del my_tuple[2] # Tampoco puede eliminarse un elemento de forma individual. 
#print(my_tuple)# NameError: name 'my_tuple' is not defined.