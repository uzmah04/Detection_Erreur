#!/usr/bin/env python3

# Fonction sum qui va calculer le checksum
def sum(arr_ascii):
	# Nombre d'element dans l'array
	x = len(arr_ascii)
	num = 0
	for i in range(x):
		# Ajouter les elements pour obtenir le checksum
		num = arr_ascii[i] + num
		
		# Pour eviter que le checksum depasse 65535, on doit faire modulo 65521
		if num > 65535:
			num = num % 65521
		
		# Stocker la somme pour pouvoir faire le deuxieme checksum
		arr_ascii[i] = num
	return num

# Demande a l'utilisateur d'inserer quelque chose
entree = input("Entrer quelque chose: ")

arr = []
arr_ascii = []

# Stocke ce que l'utilisateur a entre dans array 'arr'
for i in entree:
	arr.append(i)

# Convertir le contenu de 'arr' en ascii et le stocke dans 'arr_ascii'
for i in arr:
	arr_ascii.append(ord(i))

# Appel au fonction sum pour calculer le checksum1 et checksum2
cs1 = sum(arr_ascii)
cs2 = sum(arr_ascii)

print("Checksum2 : ", cs2)	
print("Checksum1 : ", cs1)
