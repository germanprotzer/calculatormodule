#calculadora

def calculator(one,two,accion):
    if accion == 1:
        sum = one + two
        print(sum)
    elif accion == 2:
        rest = one - two
        print(rest)
    elif accion == 3:
        multiply = one * two
        print(multiply)
    elif accion == 4:
        divide = one // two
        print(divide)
    else:
        print("you select other thing")
   


    