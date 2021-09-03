# esfera.py
# Ejercicio 1.18


cadena = input('Ingrese palabra:').lower()
vocales = ['a','e','i','o','u','á','é','í','ó','ú']
cadena_en_geringoso = ''

for caracter in cadena:
    for vocal in vocales:
        if caracter == vocal:
            cadena_en_geringoso += vocal+ 'p'
                     
    cadena_en_geringoso += caracter        

print(cadena_en_geringoso)