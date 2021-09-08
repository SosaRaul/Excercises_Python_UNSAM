# Ejercicio 5.2

import random 

# Simula una tirada.
def tirar():
    
    caras = []
    for i in range(5):
        caras.append(random.randint(1,6))

    return caras

# Devuelve True si los 5 dados salieron iguales.
def es_generala(tirada):
    
    dado_actual = 0
    pares_iguales = 0
    while(dado_actual < len(tirada)-1 and tirada[dado_actual] == tirada[dado_actual+1]):
        pares_iguales += 1
        dado_actual += 1

    return pares_iguales == 4


def prueba_estadistica(N):
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

# Simula N repeticiones y estima la prob de obtener generala en una mano de tres tiradas.
# Retorna un valor de probabilidad, 0<p<1     
def prob_generala(N):

    victorias = 0
    for i in range(N):
        # Simulacion de una mano de tres tiradas
        resultados_mano = [ es_generala(tirar()) for i in range(3)]
        for mano in resultados_mano:
            if mano:
                victorias += 1 
    
    return victorias/N            
    
print(prob_generala(200)) 
    
    
