#TUPLAS son inmutables por lo que no se puede agregar o
#cambiar datos dentro solo mostrarlos o hacer print
my_tuple = tuple()
my_other_tuple = ()

my_other_tuple = (24, "hola")
my_tuple = (35, 23, 23, "ger", "hola")
print(my_tuple)
print(type(my_tuple))

#count indica cuantos de esos elementos hay en esa lista
print(my_tuple.count("ger"))

#index indica en que posicion se encuentra el objeto a encontrar
print(my_tuple.index("hola"))

#suma de tuplas para que lasuma de tuplas se haga efectiva las tuplas
#deben tener mas de un solo elemento
nueva_tupla = my_tuple + my_other_tuple
print(nueva_tupla)

print(nueva_tupla[3:6])

my_tuple = [my_tuple]
print(type(my_tuple))

