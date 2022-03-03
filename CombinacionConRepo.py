###################################################################
####### Combinaciones de x elementos en n con repeticion ##########
###################################################################

from itertools import combinations_with_replacement

# Obtener combinaciones de 3 elementos, en 2 posiciones, con repeticion
comb = combinations_with_replacement([1, 2, 3], 2)

# Imprimir combinaciones
for i in list(comb):
	print (i)
