#Exepciones
#try: SI DA ERROR NO SE EJECUTA
#except: SE EJECUTA SI NO SE EJECUTA TRY
#else: SE EJECUTA SI SE EJECUTA TRY
#finally: SE EJECUTA SIEMPRE


a = 1
b = "2"

try:
    print(a+b)
    print("todo en orden")
except:
    print("el programa da error")
#si no se ejecuta exepcion se ejecuta el else:
else:
    print("no da error y ejecuto este else")
finally:
    print("me ejecuto siempre")

try:
    print(a+b)
except:
    print("error")