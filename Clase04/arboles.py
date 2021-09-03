def leer_arboles(nombre_archivo):
    temp = []
    arboleda = []
    dic_arboles = {}
    with open(nombre_archivo, 'rt') as file:
        informacion = next(file).split(',')
        for line in file:
            datos = line.split(',')
            i = 0
            for columna in informacion:
                dic_arboles[columna] = datos[i] 
                i += 1


    for key,value in dic_arboles.items():
        print(key,value)



  


leer_arboles("data.csv")    