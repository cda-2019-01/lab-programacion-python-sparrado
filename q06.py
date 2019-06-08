##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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

for v in unico:
    suma = (v,min([item[1] for item in datos2 if item[0]==v]),max([item[1] for item in datos2 if item[0]==v]))
    print ('{},{},{}'.format(suma[0],suma[1],suma[2]))