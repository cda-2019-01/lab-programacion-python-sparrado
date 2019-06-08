##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

#lista ordenada de vocales
col1 = [str(row[0]) for row in tabla]
values = set(col1)
values = list(values)#.sort()
values.sort()
#print (values)

#print type(tabla[1][1])

input = [(tabla[i][0],int(tabla[i][1])) for i in range(len(tabla))]
#print (input)


for v in values:
    suma = (v,max([item[1] for item in input if item[0]==v]),min([item[1] for item in input if item[0]==v]))
    print ('{},{},{}'.format(suma[0],suma[1],suma[2]))