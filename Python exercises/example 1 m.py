def contar_palabras(archivo):
    with open(archivo, 'r') as file:
        contenido = file.read()
        palabras = contenido.split()
        return len(palabras)

# Ejemplo de uso
archivo = "texto.txt" # Asegúrate de tener un archivo de texto con contenido
print(contar_palabras(archivo))