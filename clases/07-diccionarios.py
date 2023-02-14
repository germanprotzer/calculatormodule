#Diccionarios:
#funciones:del- llamado con [] -
my_dict = dict()
print(type(my_dict))

my_other_dict = {"nombre" : "german", "edad" : 34, 2:"python"}
print(my_other_dict)

my_dict = {"nombre" : "german",
           "edad" : 34,
           "Lenguajes":"python"
           }

my_dict["lenguajes"] = "hola"
print(my_dict)

#DEL: elimina un solo elemento en el diccionario
del my_dict["nombre"]
print(my_dict)

#formkeys: crea undiccionario sin valores (none)
my_new_dict = dict.fromkeys("hola")
print(my_new_dict)

