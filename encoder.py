#Cargamos las librerías necesarias.
import datetime
import time
import random


#A partir de un archivo .txt que contiene un diccionario, creamos una lista con las palabras incluidas.
dic_spa = open('diccionario.txt', encoding='utf8')
words_list=[]
for word in dic_spa:
    word = word.rstrip('\n')
    words_list.append(word)
dic_spa.close()


#Introducimos el mensaje a codificar por pantalla, lo limpiamos y lo pasamos a minúsculas.
message = input('Introduce tu mensaje a encriptar, evitando conjugar verbos: ')
message = message.strip()
message = message.lower()


#Buscamos cada una de las palabras del mensaje a codificar en la lista de palabras dada por el diccionario.
#Si la palabra no se encuentra en el diccionario, se asignará el valor -1.
split_message = message.split()
positions = []
for word in split_message:
    try:
        aux = words_list.index(word)
        positions.append(aux)
    except: 
        positions.append(-1)


#Obtenemos el día en que se va a codificar el mensaje, lo pasamos a tiempo unix y usamos este tiempo
#como semilla de aleatoriedad. Además definimos un código único de desencriptación. Con estos dos datos,
#definimos un valor aleatorio que usaremos más adelante.
day = datetime.date.today()
unixtime = time.mktime(day.timetuple())
random.seed(int(unixtime))
code = int(input('Introduce el código de desencriptación, debe ser un entero mayor que 1: '))
r_value = random.randrange(1,code)


#Las posiciones definitivas se obtendrán multiplicando las posiciones de las palabras por el valor
#aleatorio obtenido en el paso anterior.
defin_positions = []    
for num in positions:
    defin_positions.append(num * r_value)
    

#Mostramos el mensaje codificado.
print(defin_positions)
