#declarando las variables

nombre = "Jonathan"

#Variables de una sola línea
age, country, alias, age_of_experience = 27, "Guatemala", "JhoALT", 8
#No es recomendable usar este tipo de declaración de variables, ya que puede ser confuso

#Definiendo variable con camelCase
tuNombreCompletoAqui = "Mario Hugo"

#Definiendo variable con snake_case (se recomienda usar este para Python)
tu_nombre_completo_aqui = "Mario Hugo"

#concatenar con +
bienvenida = "Hola " + nombre + " ¿como estas?"

#concatenar con f-string
bienvenida = f"Hola {nombre} ¿como estas?"
print(bienvenida) 

#Concatenando con un print y separando por comas
#Se pueden concatenar variables de diferentes tipos en un solo print
print("Mi nombre es", nombre)
print("Mi nombre es", nombre, "y mi edad es", age, "años.", "Vivo en", country, "y me dicen", alias, "Cuento con", age_of_experience, "años de experiencia")
#para evitar que el texto se muestre todo junto en consola "HolaJonathan¿Como estas?" se dejan espacios
#Ya sea antes o después de cada texto para que los tome como caracteres y asi se muestre separado


#operadores de pertenencia (in / not in): está o no está
print("Lucas" in bienvenida) #"False"
print("Jonathan" not in bienvenida) #"False"
print("Jonathan" in bienvenida) #"True"

#Se pueden convertir variables de un tipo a otro con las funciones int(), float(), str(), bool() y list()
#Ejemplos:
my_int_variable = 10 #variable de tipo entero

print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) #convierte el entero a cadena de texto
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) #imprime "<class 'str'>"

my_bool_variable = False #variable de tipo booleano
print(my_bool_variable)

print(my_int_variable, my_int_to_str_variable, my_bool_variable) #imprime "10 10 False"
#Se pueden imprimir varias variables en una sola línea separándoles por comas

my_str_variable = "10" #variable de tipo cadena de texto
print(my_str_variable)

my_str_to_int_variable = int(my_str_variable) #convierte la cadena de texto a entero
print(my_str_to_int_variable)
print(type(my_str_to_int_variable)) #imprime "<class 'int'>"

#Algunas funciones del sistema
print(len(bienvenida)) #imprime la longitud de la cadena de texto
print(bienvenida.upper()) #imprime la cadena de texto en mayúsculas
print(bienvenida.lower()) #imprime la cadena de texto en minúsculas
print(bienvenida.replace("Jonathan", "Mario")) #reemplaza una cadena de texto por otra
print(bienvenida.split(" ")) #Convierte cada uno de los elementos de la cadena de texto en una lista
print(bienvenida.split(" ")[0]) #imprime el primer elemento de la lista

#Ingreso de datos con input()
nombre_usuario = input("Cual es tu nombre? ")
#Se puede ingresar texto en la consola y se almacenará dentro de la variable
edad = input("Cual es tu edad? ")
print(f"Tu nombre es {nombre_usuario} y tienes {edad} años")