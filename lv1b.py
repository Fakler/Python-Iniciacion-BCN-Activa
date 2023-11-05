# Part 2: Imagina que l’última comanda (la de 532.00 $) ha tingut un problema i només arriba el 80 % 

import math
 
# initializing tuple
dolcompres = (356.75, 487.45, 295.83, 532.00)
# calculating sum of tuple elements using math.fsum()
dolcomptotal = math.fsum(dolcompres)
#########################################################################
#Tasa de conversion
#########################################################################
print("Tasa de conversion : Canvi de dòlars a euros : 0.93195 ")
tasaconversion = 0.93195
eurocomptotal = dolcomptotal/tasaconversion
compres3total = dolcompres[3]
dolcompres3deduccion=compres3total*20/100
eurocompres3deduccion=(dolcompres3deduccion/tasaconversion)
eurocomp2total=eurocomptotal-eurocompres3deduccion
#######################################################################
#Mitjana de les quatre compres en euros
#######################################################################
nbdecompres = len(dolcompres)
euromitcompres = eurocomp2total/nbdecompres
#######################################################################
# Sabries canviar-la a una dada del tipus string?
print("Suma total de les compres en euros : " + str(eurocomp2total))
print("Mitjana de les quatre compres en euros : " + str(euromitcompres))

# Calcula, ara, els mateixos resultats que en el cas anterior i imprimeix-los per pantalla.
# Podries dir quin tipus de dada (informació) és la suma total de qualsevol dels dos casos?
print("Suma SIN deduccion")
print(type(eurocomptotal))
print("Suma CON deduccion")
print(type(eurocomp2total))


 
