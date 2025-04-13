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

#operadores de asignación
my_int = 0
my_int += 5 #my_int = my_int + 5
print(my_int)

my_int -= 2 #my_int = my_int - 2
print(my_int)

my_int *= 2 #my_int = my_int * 2
print(my_int)

my_int /= 2 #my_int = my_int / 2
print(my_int)

my_int %= 2 #my_int = my_int % 2
print(my_int)

my_int **= 2 #my_int = my_int ** 2
print(my_int)

my_int //= 2 #my_int = my_int // 2
print(my_int)

#operadores de comparación
my_int = 10
my_int2 = 20

print(my_int == my_int2)#igualdad
print(my_int != my_int2)#diferencia

print(my_int > my_int2)#mayor que
print(my_int < my_int2)#menor que
print(my_int >= my_int2)#mayor o igual que
print(my_int <= my_int2)#menor o igual que

#operadores lógicos
my_bool = True
my_bool2 = False

print(my_bool and my_bool2)#and
print(my_bool or my_bool2)#or
print(not my_bool)#not

#operadores de identidad
my_int = 10
my_int2 = 10

print(my_int is my_int2)#is
print(my_int is not my_int2)#is not

