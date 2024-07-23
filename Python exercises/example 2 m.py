def suma_columna(archivo):
    suma = 0
    with open(archivo, 'r') as file:
        for linea in file:
            valores = linea.strip().split(',')
            suma += int(valores[0])
    return suma

# Ejemplo de uso
archivo_csv = "datos.csv" # Asegúrate de tener un archivo CSV con contenido
print(suma_columna(archivo_csv))