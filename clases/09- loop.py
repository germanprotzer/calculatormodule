#while-For:

#while
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
    if my_condition == 8:
        break

print("Mi condicion no cumple")

#For: esta atado a cuantos
#elementos en mi lista o tupla o set o dict

print("list:")
my_list = [22,12,42,56,78]
for element in my_list:
    print(element)

tupla = (22,12,33)
set = {12,45,89}
dicc = {12:12, 34 : 34 , 89: 12}

#Tuple: colecciones de datos idénticos o distintos clasificados
#  con un índice y que no pueden ser modificados.
print("tupla:")
for element in tupla:
    print(element)

#set: es una colección desordenada de elementos únicos, es 
# decir, que no se repiten.
print("set:")
for element in set:
    print(element)

#dicc: nos permiten almacenar una serie de mapeos entre dos 
# conjuntos de elementos, llamados keys and values
print("dicc:")
for element in dicc:
    print(element)

