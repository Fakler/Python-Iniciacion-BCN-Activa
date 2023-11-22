#Pomes: 3,56 €
#Mandarines: 4,35 €
#Síndria: 6,23 €
#Maduixes: 4,28 €
#Peres: 2,86
#Taronges: 3,48
#Dictionaries
"""
Guardar en una nova variable la llista dels imports
sense tenir en compte els dos últims
"""

fruites_dict = dict(Pomes= 3.56, Mandarines=4.35, Síndria=6.23, Maduixes=4.28, Peres=2.86, Taronges=3.48)
nb_de_compras = (len(fruites_dict))
val_fruites = fruites_dict.values()
fruites_val_llista = list(val_fruites)
nueva_llista_dels_imports = fruites_val_llista[0:4]
print(nueva_llista_dels_imports)