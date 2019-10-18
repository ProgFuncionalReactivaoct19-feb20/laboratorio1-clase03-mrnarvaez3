"""
	Problema 2:
	Dada la siguiente lista:
	notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
	En contrar una lista como sigue:
	[20, 16, 20, 15]
	
	Roberto Narvaez
"""
#  Datos del problema
notas = [(5, 5, 10), (10, 2, 4), (10, 1, 9), (10, 2, 3)]
#  Asigno posicion de cada tupla
suma1 = lambda x: x[0]
suma2 = lambda x: x[1]
suma3 = lambda x: x[2]
#  Hago la suma de todas las posiciones
sumaTotal = lambda x: suma1(x)+suma2(x)+suma3(x)

#  Salida de datos
print(list(map(sumaTotal ,notas)))

