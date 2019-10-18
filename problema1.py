"""
	Problema 1:
	Dado el siguiente conjunto de promedios de estudiantes; determinar los 
	estudiantes que pasan de ciclo. Todos los estudiantes que pasan de ciclo
	son aquellos que tienen un promedio de 16.5 o mayor.
	promedios.txt
	
	Roberto Narvaez
"""

#  Abro el archivo en una variable
archivo = open("promedios.txt")
#  De mi variable llena con los datos los leo
datos = archivo.read()
 
#  La hago lista y seguidamente entero para poder trabajarla
list(datos)
x = datos.split(',')

x = list(map(int, x))
#  la condicion para obtener mi resultado
resultado = filter(lambda x: x>= 16.5, x)

#  Salida de datos
print(list(resultado))
