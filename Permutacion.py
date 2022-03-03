###################################################################
####### Permutaciones de todos los elementos sin repeticion #######
###################################################################

from itertools import permutations

#Obtener permutaciones de 1, 2 y 3
perm = permutations([1, 2, 3])

# Imprimir
for i in list(perm):
	print (i)
