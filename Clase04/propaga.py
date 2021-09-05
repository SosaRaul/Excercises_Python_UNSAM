# Quema los 0 consecutivos, empezando del final de la lista.
def quemar_izq(lista):
    
    # Quema la lista izquierda.
    i = -1
    while( i >= -len(lista) and lista[i] == 0):
        lista[i] = 1
        i -= 1

    return lista        
        
# Quema los 0 consecutivos empezando del ppio de la lista.
def quemar_der(lista):
    
    # Quema la lista derecha
    i = 0
    while( i < len(lista) and lista[i] == 0):
        lista[i] = 1
        i += 1

    return lista        


# Propaga 1 sobre todos los 0 que le continuan hacia izq y der. Para si se encuentra con un numero distinto.
def propagar(lista):

    for i in range(0, len(lista)):
        
        if(lista[i] == 1):
            # Propago a la sublista izquierda.
            lista[:i] = quemar_izq(lista[:i])
            # Propago a la sublista derecha.
            lista[i+1:] = quemar_der(lista[i+1:])



# Pruebitas.
lista =  [-1*((i% 6)//2-1) for i in range(60) ]
print("lista original  : ",lista)
propagar(lista)
print("lista propagada : " ,lista)