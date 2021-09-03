# Retorna lista invertida
def invertir_lista(lista):

    lista_invertida = []

    for indice in range(1, len(lista)+1):
        lista_invertida.append(lista[-indice])

    return lista_invertida

# Ejemplos
print(invertir_lista([1,10,1,50,45,0]))  
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))          