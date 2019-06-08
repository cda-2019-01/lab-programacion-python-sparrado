##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
fecha = [row[2].split('-') for row in archivo]
mes = [row[1] for row in fecha]
mes.sort()
q04 = collections.Counter(mes)
q04