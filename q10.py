##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
import csv
with open('data.csv', 'rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    tabla = list()
    for fila in csv_reader:
        tabla.append(fila)

#print (tabla)
datos = [str(row[4]).split(',') for row in tabla]
#print (datos)

#unir en una sola lista
datos1 = [data for sublist in datos for data in sublist]
#print (datos1)

#se crea una lista de lista [clave, valor]
datos2 = [(dato.split(':')) for dato in datos1]
#print (datos2)

#crear lista de claves
total_claves = [clave[0:3] for clave in datos1]
#print (total_claves)
unico = set(total_claves)
unico = list(unico)
unico.sort()

#print (unico)

salida = [(key,total_claves.count(key)) for key in unico]

for tupla in salida:
    print ("{},{}".format(tupla[0],tupla[1]))
