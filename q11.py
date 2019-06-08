##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

#print (tabla)

tabla1 = [(i[0],len(i[3].split(',')),len(i[4].split(','))) for i in tabla]
#print (tabla1)

for i,j,k in tabla1:
    print ("{},{},{}".format(i,j,k))