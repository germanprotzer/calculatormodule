#REGULAR EXPRESIONS:(abarca muchos terminos)
#permite analizar si una cadena de texto tiene cosas


import re

my_string = "this is my life : i want to share it with you <3 "
my_other_string = "hello world" 

# MATCH: permite encontrar un patron
# (debe coincidir desde el principio)
print("MATCH:")


print(re.match("this is my life", my_string))

#PRINTEO:
# <re.Match object; span=(0#ESTA ES LALINEA#, 15 ), 
# match='this is my life'> 

#No lo encuentra porque busca desde el principio y 
# devuelve none:
print(re.match("my life", my_string))

#COMO COMPROBAR NONE:
print("RE.I:")


match = re.match("this is my life", my_string, re.I)
print(match)
print(match.span())#in which line is what i want to search
start, end = match.span() #I create the variables to start and end
print(my_string[start:end]) #I select what i want to print abaout the string

#Hacer que el NONE nos devuelva una frase:

match = re.match("hello world", my_other_string)
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

#SEARCH: find it where ever is the phrase in the string
print("SEARCH:")

search = re.match("this is my life", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

#FINDALL: finds in array form 
print("FINDALL:")

findall = re.findall("this is my life", my_string, re.I)
print(findall)

#SPLIT: it divide the string when it finds a patron in the sentence
print("SPLIT:")

Split = re.split("is", my_string)
print(Split)

#SUB: substitut what i want to change












