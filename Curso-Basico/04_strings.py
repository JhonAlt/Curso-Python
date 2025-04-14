###Strings###

my_string = "Mi string"# Se puede utilizar comillas dobles para las cadenas de texto
my_other_string = 'Mi otro string'# O se pueden utilizar comillas simples

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = 'Este es un string \ncon salto de linea'
print(my_new_line_string)

my_tab_string = '\tEste es un string con tabulación'
print(my_tab_string)

my_scape_string = '\tEste es un string \nescapado'
print(my_scape_string)

##Formateo##

name, surname, age = 'Jonathan', 'Amezquita', 27

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) # En .format se utilizan llaves.

print('Mi nombre es %s %s y mi edad es %d' %(name, surname, age)) # En este se utilizan los símbolos de porcentaje.
# Se utiliza %s para los strings y %d para los números.
print(f'Mi nombre es {name} {surname} y mi edad es {age}') # Formateo con f strings

## Desempaquetado de caracteres ##

language = 'Python'
a, b, c, d, e, f = language # Las siguientes líneas utilizan la función print() para mostrar el valor de cada variable
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)# Como resultado, cada carácter de la palabra 'Python' se imprimirá en una línea separada:

## Division ##

language_slice = language[1:3]# Indica que se desea obtener los caracteres desde el índice 1 (incluido) hasta el índice 3 (excluido).
print(language_slice)

language_slice = language[1:]# Se extraerán todos los caracteres desde el índice 1 hasta el final de la cadena.
print(language_slice)

language_slice = language[-2]
print(language_slice)

'''
Este fragmento de código demuestra cómo extraer subcadenas específicas utilizando índices, 
lo cual es útil en muchas aplicaciones como el procesamiento de texto o la manipulación de datos.
'''
## Reverse ##

reverse_language = language[::-1]# Selecciona todos los caracteres de la cadena, pero en orden inverso.
print(reverse_language)

## Funciones ##

print(language.capitalize())# convierte el primer carácter de la cadena en mayúscula y el resto en minúsculas.
print(language.upper())# convierte todos los caracteres de la cadena a mayúsculas.
print(language.count('t'))# cuenta cuántas veces aparece un carácter o subcadena específica en la cadena.
print(language.isnumeric())# Este método verifica si todos los caracteres de la cadena son numéricos.
print('1'.isnumeric())# Aquí se aplica el método isnumeric() directamente sobre la cadena
print(language.lower())# Este método convierte todos los caracteres de la cadena a minúsculas.
print(language.startswith('Py'))# Este método verifica si la cadena comienza con una subcadena específica.