#dates
# datetime: module supplies classes for manipulating dates and times.
# While date and time arithmetic is supported, the focus of the 
# implementation is on efficient attribute extraction for output 
# formatting and manipulation

#Time: provides various time-related functions. For related 
# functionality, see also the datetime and calendar modules

#datetime: agrupa hora y fecha
from datetime import datetime

now = datetime.now()
print(now)
print("ESTO ES DATETIME:")
year_2023 = datetime(2023,6,1)

print(year_2023)
print(year_2023.year)
print(year_2023.month)
print(year_2023.day)


#Time: agrupa la hora
print("ESTO ES TIME:")

from datetime import time

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#Date: agrupa la fecha

print("ESTO ES DATE:")
from datetime import date

date_time = date(2023,4,2)

print(date_time.year)
print(date_time.month)
print(date_time.day)

date_time = date(date_time.year, date_time.month + 1, date_time.day)

print(date_time.month)

#diff : esta variable resta las dos 
#funciones siempre y cuando tengan los mismos formatos de fechas
diff = year_2023 - now
print(diff)

#Timedelta: es para trabajar con franjas de fechas (ejemplo: la 
# suscripcion de una prsona donde yo quiero saber cuanto tiempo 
# estuvo suscripto por lo cual sumo cuanto tiempo estuvo en cada 
# lapso de tiempo)

print("ESTO ES TIMEDELTA:")

from datetime import timedelta

time_delta = timedelta(200,100,23,weeks=3)
time_delta_dos = timedelta(300,400,53,weeks=1)

print(time_delta - time_delta_dos)
print(time_delta + time_delta_dos)












