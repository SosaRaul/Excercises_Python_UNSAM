# Retorna el indice de la ultima coincidencia del elemento en la lista.
def buscar_u_elemento(lista,elemento_buscado):
    
    indice_buscado = -1

    for indice in range(0,len(lista)):
        if(lista[indice] == elemento_buscado):
            indice_buscado = indice 

    return indice_buscado

# Retorna la cantidad de veces que aparece un elemento en la lista.       
def buscar_n_elemento(lista,elemento_buscado):

    coincidencias = 0

    for indice in range(0,len(lista)):
        if(lista[indice] == elemento_buscado):
            coincidencias += 1

    return coincidencias

# Retorna el mayor elemento de una lista numérica.
def maximo(lista):

    maximo = lista[0]

    for elemento in lista:
        if elemento > maximo:
            maximo = elemento

    return maximo        

# Retorna el menor elemento de una lista numérica
def minimo(lista):

    minimo = lista[0]

    for elemento in lista:
        if elemento < minimo:
            minimo = elemento

    return minimo        





# Ejemplitos de prueba.

print("Coincidencias : ",buscar_n_elemento([1,0,100,100,110],100))            
print("Minimo : ",minimo([10,-8,5,2,3]))
print("Maximo : ",maximo([10,-89,100,1,3]))
