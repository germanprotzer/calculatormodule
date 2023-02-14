#Files handing:
import os

# .txt file

txt_file = open("Holamundo.txt" , "w+")
txt_file.write("soy el gercho\nque onda\nalguien por ahi")

#print(txt_file.read())
#Leer las palabras que seleccionemos
#print(txt_file.read(10))
#Leer linea 
#print(txt_file.readline())
#Leer todas las lineas
#print(txt_file.readlines())

#Agregar texto
for line in txt_file.readlines():
    print(line)
#BP: Close the file when i finished
txt_file.close()

#Borrar el fichero:
#os.remove("NOMBRE DEL ARCHIVO Y O RUTA")
#EJ:  os.remove("Holamundo.txt")


print("JSON:")

#JSON FILE:
#tipo de dato muy utilizado en el ambito web porque
#es tipo de señalizacion para poder codificar datos.

import json

#Primero se crea el archivo json con OPEN()
json_file = open("json_file.json" , "w+")

#IMPORTANTE: las claves de los json deben ser string
json_test = {"nombre" : "german", "edad" : 34, "hola" : "python"}

print("dump:")
#Dump: Esta es una función que toma dos argumentos:
#*El objeto que será almacenado en formato JSON (por ejemplo, un diccionario).
#*El archivo en el cual será almacenado (un objeto archivo).

#Pasar del DICCIONARIO de arriba a un JSON: 
json.dump(json_test, json_file)
#indent: crea espacios delante de la linea de las claves
#json.dump(json_test, json_file, indent = 4)

#BP: PARA PODER LEER 
json_file.close()

with open("json.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

#Creo un DICCIONARIO con el archivo JSON:
json_dict = json.load(open("json_file.json"))
print(json_dict)

print("CSV:")
import csv

csv_file = open("csv_file.csv" , "w+")

#Como escribir en csv file:
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","lastname","age","languaje","website"])
csv_writer.writerow(["ger","protzer","22","spanish","gr.com"])

csv_file.close()

with open("csv_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


