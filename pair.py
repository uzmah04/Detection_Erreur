#!/usr/bin/env python3

# Demande a l'utilisateur d'inserer quelque chose
# Tous les entrees de l'utilisateur est considerer comme un string
entree = input("Entrer quelque chose: ")

# Convertir string en binaire
binaire = ''.join(format(i, 'b') for i in bytearray(entree, encoding ='utf-8')) 

# Mettre le binaire dans un array
arr = [binaire]
print(arr)

# Parcourir le array pour conter le nombre de "1"
for i in arr:
	a = 0
	for j in i:
		if '1' in j:
			a = a + 1

# Si le array a un nombre pair de "1", le programme va ajouter "0" devant la suite binaire			
if a%2==0:
	binaire = "0" + binaire
# Si le array a un nombre impair de "1", le programme va ajouter "1" devant la suite binaire
else:
	binaire = "1" + binaire

print("Bit de parite pair : ", binaire)
