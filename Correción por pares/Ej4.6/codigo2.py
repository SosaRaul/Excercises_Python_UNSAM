##propaga.py
##Ejercicio 4.6: Propagación
#imaginar una fila con varios fósforos uno al lado del otro.
#Los fósforos pueden estar en tres estados, representados en una lista
#nuevos: 0, encendidos: 1, carbonizado: -1
#función 'propagar(lista)' que 
#reciba un vector con 0's, 1's y -1's
#devuelva un vector en el que los 1's se propagaron a sus vecinos 0's

def propagar(lista):
	'''Recibe un vector con 0´s, 1's y -1´s.
	Devuelve un vector en el que los 1's se propagaron a sus vecinos 0´s
	'''
	#Lista auxiliar vacía que guarda los primeros valores
	lista_propagada = []
	#Lista auxiliar vacía para recorrer en forma inversa
	propagada_invertida = []
	#Lista auxiliar vacía  para guardar nuevos valores
	lista_propagada2 =[]
	#Lista auxiliar vacía para devolver los resultados en el orden correcto
	propagada2_invertida = []
	#Lista auxiliar vacía para guardar seguidilla de 0´s
	lista_0=[]

	#Recorrer la lista de entrada con sus índíces
	for i, e in enumerate(lista):
		#Analizar cada elemento de la lista, mientras no sea el último
		if i < (len(lista)-1):
			#Si el elemento es un 0, mirar el elemento siguiente
			if e == 0:
				if lista[i+1] == 0:
					lista_0.append(e)
				elif lista[i+1] == 1:
					lista_0.append(e)
					for z in lista_0:
						z = 1
						lista_propagada.append(z)
					lista_0 = []
				elif lista[i+1] == -1:
					lista_0.append(e)
					for z in lista_0:
						lista_propagada.append(z)
					lista_0 = []
			#Si el elemento es un 1, se añade directamente		
			elif e == 1:
				lista_propagada.append(e)
			#Si el elementos es un -1, se añade directamente	
			else:
				lista_propagada.append(e)
		#Analizar el último elemento, no se puede chequear el siguiente
		#Añadir todos los 0´s que no hayan sido modificados		
		else:
			lista_propagada.append(e)
			if len(lista_0) > 0:
				for z in lista_0:
					lista_propagada.append(z)
				lista_0 = []
	#invertir lista-resultado para volver a recorrerla	
	for e in lista_propagada:
		propagada_invertida = [e] + propagada_invertida
	#Mismo análisis, pero con la lista ya procesada una vez e invertida	
	for i, e in enumerate(propagada_invertida):
		if i < (len(propagada_invertida)-1):
			if e == 0:
				if propagada_invertida[i+1] == 0:
					lista_0.append(e)
				elif propagada_invertida[i+1] == 1:
					lista_0.append(e)
					for z in lista_0:
						z = 1
						lista_propagada2.append(z)
					lista_0 = []
				elif propagada_invertida[i+1] == -1:
					lista_0.append(e)
					for z in lista_0:
						lista_propagada2.append(z)
					lista_0 = []
			elif e == 1:
				lista_propagada2.append(e)
			else:
				lista_propagada2.append(e)
		else:
			lista_propagada2.append(e)
			if len(lista_0) > 0:
				for z in lista_0:
					lista_propagada2.append(z)
				lista_0 = []
	#invertir lista-resultado para devolver los valores en su lugar correspondiente
	for e in lista_propagada2:
		propagada2_invertida= [e] + propagada2_invertida
	return propagada2_invertida

def main():
	print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
	print(propagar([ 0, 0, 0, 1, 0, 0]))
	'''
		>>> main()
		[0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
		[1, 1, 1, 1, 1, 1]
	'''
	