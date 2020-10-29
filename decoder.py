#Cargamos las librerías necesarias.
import datetime
import time
import random
import os


#A partir de un archivo .txt que contiene un diccionario, creamos una lista con las palabras incluidas.
dic_spa = open('diccionario.txt', encoding='utf8')
words_list=[]
for word in dic_spa:
    word = word.rstrip('\n')
    words_list.append(word)
dic_spa.close()


#Introducimos los valores del mensaje codificado, separados por comas.
defin_positions = input('Introduce los valores del mensaje encriptado, separados por comas: ')
defin_positions = defin_positions.split(',')


#Introducimos el código único de desencriptación.
code = int(input('Introduce el código de desencriptación: '))


#Obtenemos el día en que fue codificado el mensaje.
encode_day = os.path.getmtime('encoder.py')
encode_day = datetime.datetime.fromtimestamp(encode_day)
encode_day = encode_day.isoformat()
day_aux = encode_day[0:10].split('-')
day = [int(day_num) for day_num in day_aux]
    

#Convertimos el día de codificación en tiempo unix y con el código de desencriptación, obtenemos
#el valor aleatorio necesario.
day = datetime.date(*day)
unixtime = time.mktime(day.timetuple())
random.seed(int(unixtime))
r_value = random.randrange(1,code)


#Obtenemos las posiciones originales de las palabras en el diccionario dividiendo entre el valor aleatorio.
positions = []    
for num in defin_positions:
    num = int(num)
    if r_value <= num:
        num_def = num // r_value
        positions.append(num_def)
    else:
        r_new = r_value % num
        num_def = num // r_new
        positions.append(num_def)


#Con las posiciones, buscamos las palabras en la lista de palabras del diccionario, y devolvemos una lista.
words = []
for num in positions:
    if num >= 0:
        word = words_list[num]
        words.append(word)
    else:
        words.append('[]')


#Convertimos la lista de palabras a cadena de texto. Mostramos el mensaje original.
message = ' '.join(words)
message = message.capitalize()
print(message)
