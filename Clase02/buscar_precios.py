# Ej 2.7
# Busca precio de una fruta en un .csv y lo imprime, sino la encuentra deja un msj.
def buscar_precios(fruta):
    # Apertura de archivo e inicialización de flag
    data = open('camion.csv', 'rt')
    encontrada = False
    # Búsqueda en el archivo
    for line in data:
        row = line.split(',')
        if(fruta.lower() == row[0].lower()):
            encontrada = True
    # Acciones post-búsqueda
    if(encontrada):
        print(f'El precio de un cajón de {fruta} es: ',row[2])
    else:
        print(f'{fruta} no figura en el listado de precios.')    
    # Cierre de archivo
    data.close()

fruta = input('Ingrese fruta: ')
buscar_precios(fruta)    