
'''
1. Declara una variable text con la frase “Aprendiendo Python”
y luego imprime la longitud de la cadena usando len().
'''
text = 'Aprendiendo Python'
print(len(text))

'''
2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
'''
print('Hola ' + 'Python')

'''
3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
'''
print('Esta es una cadena \ncon salto de línea')

'''
4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, 
apellido y edad en una cadena de texto.
'''
name = 'Jonathan'
last_name = 'Álvarez'
age = 27

print(f'Hola mi nombre es {name} {last_name} y tengo {age} años')

'''
5. Desempaqueta los caracteres de la palabra “Python” 
en variables separadas y luego imprímelos uno por uno.
'''
language = 'Python'
a, b, c, d, e , f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

'''
6. Extrae un “slice” de la palabra “Programación” 
para obtener los caracteres desde la posición 3 hasta la 7.
'''
palabra = 'Programación'
print(palabra[3:7])
print(len(palabra))

'''
7. Invierte la cadena “Python” usando slicing y muestra el resultado.
'''
print(language[::-1])

'''
8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
'''
print(text.upper())

'''
9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
'''
text2 = 'Programación en Python'
print(text.count('n'))

'''
10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
'''
cadena = '12345'
print(cadena.isnumeric())