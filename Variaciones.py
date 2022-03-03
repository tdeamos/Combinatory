###################################################################
####### Variaciones de x elementos en n  sin repeticion ###########
###################################################################

from itertools import permutations

# Obtener variaciones de 3 elementos, en 2 posiciones
perm = permutations([1, 2, 3], 2)

# Imprimir
for i in list(perm):
	print (i)


