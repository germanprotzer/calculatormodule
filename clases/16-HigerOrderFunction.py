#Higher Orders functions: Estan en 
# lo mas alto a nivel de jerarquia de datos


def sum_two_values(values):
    return values + 3

def sum_two_add_one(one,two,f):
    return f(one + two)

print(sum_two_add_one(1,5,sum_two_values))

#closures: 
# Closure in Python is an inner function object, 
# a function that behaves like an object, that remembers and 
# has access to variables in the local scope in which it was 
# created even after the outer function has finished executing.
print("CLOSURES:")

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))

#Map: recorre todos los valores para ejecutar una
#funcion sobre ellos
print("MAPS:")

numbers = [2,5,10,21]

def multiply_two(number):
    return number * 2

#map(list(map(multiply_two,numbers)))
#map(list(map(lambda number: number * 2,numbers)))

#Filter: recorre todos los valores para ejecutar un true
# o false para filtrar el valor de los iterados 

def filter_greater_than_ten(number):
    if number > 10:
        return True
    

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))
