## Operadores aritméticos en Python

#suma y resta (+ y -)
suma = 12 + 5
resta = 12 - 5
print(suma)
print(resta)

#multiplicación y división (* y /)
multi = 12 * 5
division = 12 / 5 #siempre devuelve un dato float 
print(multi)
print(division)

#potenciación/exponente (**)
exponente = 12 ** 5
print(exponente)

#división baja (//)
division_baja = 12 // 5 #devuelve entero redondeado hacia abajo
print(division_baja)

#Modulo (%)
resto = 12 % 5
print(resto)

print("Hola al numero: " + str(12))#concatenar un entero a un string 
print("Hola " * 5)# si es posible multiplicar un string por un entero
print("Hola " * (2**3))#Esto ya es solo por probar XD

my_float = 2.5 * 2 #Esto da como resultado 5.0
#print("Hola " * my_float)#Esto da un error porque no se puede concatenar un float a un string
print("Hola " * int(my_float))#Esto convierte el float a un entero y lo concatena a un string