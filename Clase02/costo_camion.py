# Apertura del archivo e inicialización del acumulador
data = open('camion.csv', 'rt')
costo_total = 0
# Skipeo el encabezado de la tabla.
headers = next(data)
# Tomo cada linea del archivo y obtengo el costo por cajon , que luego acumulo,.
for line in data:
    row = line.split(',')
    costo_total += float(row[1])*float(row[2])
# Muestro costo total por pantalla y cierre de archivo.    
print(costo_total)
data.close()