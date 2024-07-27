def frecuencia_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

# Ejemplo de uso
texto = "Esta es una cadena de texto con palabras, algunas se repiten y otras no."
print(frecuencia_palabras(texto))