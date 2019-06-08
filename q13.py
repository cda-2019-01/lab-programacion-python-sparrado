##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

tabla1 = [(i[0],i[4].split(',')) for i in tabla]
"""
tabla2 =  []
for linea in tabla1:
    temp = tuple()
    print(linea[0])
    for codigo in linea[1]:
        suma=0
        suma = suma +int(codigo[-1])
        print (suma)
"""
for i in range(len(tabla1)):
    #print (tabla1[i][1])
    a=0
    for j in range(len(tabla1[i][1])):
        #print (tabla1[i][1][j][-1])
        
        a += int(tabla1[i][1][j][-1])
    print ("{},{}".format(tabla1[i][0],a))