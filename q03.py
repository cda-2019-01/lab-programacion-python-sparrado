##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
q03 = []
for i, g in groupby(sorted(archivo), key=lambda x: x[0]):
    q03.append([i, sum(row[1] for row in g)])

for i in q03: print(i)