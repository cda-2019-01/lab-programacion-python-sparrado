##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

inicio = []
indice = []
for linea in tabla:  
    temp1 = [(int(linea[1]),letra) for letra in linea[3].split(',')]
    temp2 = [letra for letra in linea[3].split(',')]
    inicio += temp1
    indice += temp2

indice1 = set(indice)
#print(indice1)
indice1 = list(indice1)
indice1.sort()


for letra in indice1:
    a=0
    for i,j in inicio:
        if letra == j:
            a += i
    print ("{},{}".format(letra,a))