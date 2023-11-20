#Pomes: 3,56 €
#Mandarines: 4,35 €
#Síndria: 6,23 €
#Maduixes: 4,28 €
#Peres: 2,86
#Taronges: 3,48
#Dictionaries
'''
Podries calcular la mitjana de la compra accedint als valors de les claus? Procura posar només dos decimals.
Podries copiar i guardar en una nova variable la llista dels imports sense tenir en compte els dos últims?
Podries saber com comprovar si hem comprat llimones?
'''

fruites_dict = dict(Pomes= 3.56, Mandarines=4.35, Síndria=6.23, Maduixes=4.28, Peres=2.86, Taronges=3.48)
p_pomes = fruites_dict.get('Pomes')
p_mandarines = fruites_dict.get('Mandarines')
p_sindria = fruites_dict.get('Síndria')
p_maduixes = fruites_dict.get('Maduixes')
p_peres = fruites_dict.get('Peres')
p_taronges = fruites_dict.get('Taronges')

sum_fruites = sum(value for value in [p_pomes, p_mandarines, p_sindria, p_maduixes, p_peres, p_taronges] if value is not None)

# calcular 1 - la mitjana de la compra 2 - pormedio
nb_de_compras = (len(fruites_dict))
mitjana_de_compras = sum_fruites / nb_de_compras
print ("Mitjana de la compra : ", mitjana_de_compras)