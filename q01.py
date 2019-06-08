##
## Imprima la suma de la segunda columna.
##
##x = pandas.read_csv('datos.csv',
##                     sep = ';',
##                    thousands = None,
##                     header = None,
##                     decimal = '.')
##p1 = x[1].sum()
##print(p1)##
import csv
import math
import pandas as pd
from operator import itemgetter
from itertools import groupby
import collections

### leo el archivo y convierto la segunda columna en int
archivo = open('datos.csv', 'r').readlines()
archivo = [row[0:-1] for row in archivo]
archivo = [row.split(';') for row in archivo]
archivo = [[row[0], int(row[1]), row[2], row[3], row[4]] for row in archivo]
##archivo
## sumo la primera columna de cada fila, que es una lista
q01 = sum([row[1] for row in archivo])
q01