#variables
myvariable = "My strings"
print(myvariable)

#Aca se demuestra como el tipado es dinamico
# y cambia no importa que la
#variable haya sido un entero

my_int_variable = 5
print(my_int_variable)

my_int_to_variable = str(my_int_variable)
print(type(my_int_to_variable))

my_bool_variable = False
print(my_bool_variable)

#concatenación de una variable
print(my_int_variable, my_int_to_variable , my_bool_variable)

#Funciones del sistema (Cuenta cuantos caracteres tiene la variable)
print(len(my_int_to_variable))

#Variables en una sola linea:

name, surname, alias, age = "Brais" ,"Moure","ger", 35
print(name,surname,alias,age)

#Inputs

name = input("Cuantos años tienes?")
age = input("Cual es tu edad?")

print(name)
print(age)




