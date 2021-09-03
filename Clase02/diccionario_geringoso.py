# Funcion que recibe un string y retorna su geringoso
def geringoso(cadena):
    cadena = cadena.lower()
    vocales = ['a','e','i','o','u','á','é','í','ó','ú']
    cadena_en_geringoso = ''

    for caracter in cadena:
        for vocal in vocales:
            if caracter == vocal:
                cadena_en_geringoso += vocal+ 'p'
                        
        cadena_en_geringoso += caracter 

    return cadena_en_geringoso   
# Lista de prueba, se puede cambiar a un ingreso del usuario
lista_palabras = ['alberto','pedro','juan']
# Inicializo el diccionario
dic = {}
# Recorro la lista y voy creando los pares clave:valor en el dic.
for palabra in lista_palabras:
    dic[palabra] = geringoso(palabra)

print(dic)    