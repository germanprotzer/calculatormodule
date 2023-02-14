#Funciones
nombre = "german"
apellido = "hola"
salsa = 33
def my_function (apellido):
  nombre = "hernan"

print(nombre)

#el asterisco en el def hace que podamos agregar los parametros que querramos

def print_text (*polo):
    print(polo)

print_text("hola", "manola")
print_text("que onda")