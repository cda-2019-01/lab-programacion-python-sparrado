##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)


dat1 = [int(row[1]) for row in tabla]
dat2 = [str(row[0]) for row in tabla]
entrada = [(row[1],str(row[0])) for row in tabla]
#print(entrada)
unico1 = set(dat1)
unico1 = list(unico1)
unico1.sort()
unico_str = [str(value) for value in unico1]

#print(unico_str)
salida = [(x,[y for z,y in entrada if x==z]) for x in unico_str]

salida1 = [(x,sorted(y)) for x,y in salida]

for linea in salida1:
    print (linea)
