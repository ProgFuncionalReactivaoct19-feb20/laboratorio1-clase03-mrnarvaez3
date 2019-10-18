"""
Problema 5:
	Dadas las siguientes edad:
	[10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]
	Se ha generado una lista denomindad black_edades, formada así:
	[10, 14, 30, 32, 40, 16]
	Generar el listado de edades que no estén dentro de las black_edades.
	12,13,18,20,31,33,50
	Roberto Narvaez
"""

#  metodo donde le envio la lista con todas las edades
def gen_edades (x):
	black_edades = [10, 14, 30, 32, 40, 16]
#  condicion para obtener resultado final
	if x in black_edades:
		return False
	else:
		return True

edades = [10, 12, 13, 14, 16, 18, 20, 30, 31, 32, 33, 40, 50]

#  obtencion y salida de datos
resultado = filter(gen_edades, edades)

print(list(resultado))
