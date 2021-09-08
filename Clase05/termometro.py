# Ejercicio 5.6
import random

def media(muestra):
    return round(sum(muestra)/len(muestra),2)

def mediana(muestra):
   
    n = len(muestra)
    # Ordeno la lista 
    muestra_ordenada = sorted(muestra)
    # Muestra de una longitud par
    if(n%2 == 0):
        return round((muestra_ordenada[(n-1)//2] + muestra_ordenada[(n-1)//2 +1])/2,2)
    # Muestra de una longitud impar
    else:
        return muestra_ordenada[(n)//2]



def medir_temp(n,mu,sigma):
   
    mediciones = [(37.5 + round(random.normalvariate(mu,sigma),2))for i in range(n)]
    return mediciones

def resumen_temp(n):
    
    muestra = medir_temp(n,0,0.2)
    valor_max = max(muestra)
    valor_min = min(muestra)
    promedio_muestra = media(muestra)
    mediana_muestra = mediana(muestra)

    return valor_max, valor_min, promedio_muestra, mediana_muestra
    
    
    
print(resumen_temp(10))