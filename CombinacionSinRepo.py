###################################################################
####### Combinaciones de x elementos en n sin repeticion ##########
###################################################################

from itertools import combinations

# Obtener combinaciones de 3 elementos, en 2 posiciones
comb = combinations([1, 2, 3], 2)

# Imprimit combinaciones
for i in list(comb):
	print (i)

###################################################################

# Obtener combinaciones de 3 elementos, en 2 posiciones, de diferente orden. Que ocurrira?
comb = combinations([2, 1, 3], 2)

# Imprimit combinaciones
for i in list(comb):
	print (i)

###################################################################

# Obtener combinaciones de 3 elementos, en 3 posiciones. Que ocurrira?
comb = combinations([1, 2, 3], 3)

# Imprimit combinaciones
for i in list(comb):
	print (i)
