import math
 
# initializing tuple
dolcompres = (356.75, 487.45, 295.83, 532.00)
 
# calculating sum of tuple elements using math.fsum()
dolcomptotal = math.fsum(dolcompres)
 
# printing result
print("Suma total de compras en dolares : " + str(dolcomptotal))
#########################################################################
#Tasa de conversion
# la variable que necessitaràs per tenir el canvi de dòlars a euros rebi la dada a través d’una entrada per teclat
#########################################################################
print("Tasa de conversion : Canvi de dòlars a euros : ")
tasaconversion = float(input())
eurocomptotal = dolcomptotal/tasaconversion
#######################################################################
#Mitjana de les quatre compres en euros
#######################################################################
nbdecompres = len(dolcompres)
euromitcompres = eurocomptotal/nbdecompres
#######################################################################
print("Suma total de les compres en euros : " + str(eurocomptotal))
print("Mitjana de les quatre compres en euros : " + str(euromitcompres))












 

