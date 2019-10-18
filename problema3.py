"""
Problema 3:
	Dada la siguiente frase:
	"No hay medicina que cure lo que no cura la felicidad"
	Encuentre el listado que sigue:
	["No", "hay", "que", "lo", "que", "no", "la"]

	Roberto Narvaez
"""

cadena ="No hay medicina que cure lo que no cura la felicidad"
#  pongo el separador de mi cadena en una variable
separador = " "
#  la separo la cadena segun la variable
lista = cadena.split(separador)


resultado = filter(lambda x: len(x)<=3, lista)
#  salida de datos
print(list(resultado))


