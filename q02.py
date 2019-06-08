##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
##x = pandas.read_csv('datos.csv',
  ##                   sep = ';',
    ##                 thousands = None,
      ##               header = None,
        ##             decimal = '.')
##p2
##x.sort_values(0)
##p2 = x[0].value_counts().sort_index()
##print(p2)
######################################
import csv
import math
import pandas as pd
from operator import itemgetter
from itertools import groupby
import collections

archivo = open('datos.csv', 'r').readlines()
archivo = [row[0:-1] for row in archivo]
archivo = [row.split(';') for row in archivo]
archivo = [[row[0], int(row[1]), row[2], row[3], row[4]] for row in archivo]
########################3
Col1 = [row[0] for row in archivo]
Col1.sort()
q02 = collections.Counter(Col1)
q02