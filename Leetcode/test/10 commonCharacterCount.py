#Given two strings, find the number of common characters between them, if the character is repeated count how many times it is repeated.

def solution(s1, s2):
    # Crear un conjunto de caracteres únicos en s1
    s1_set = set(s1)
    # Inicializar el contador de coincidencias
    coincidencias = 0
    # Iterar sobre los caracteres únicos de s1
    for char in s1_set:
        # Contar la cantidad de veces que aparece el carácter en s1 y s2
        coincidencias += min(s1.count(char), s2.count(char))
    
    return coincidencias
    
if __name__ == '__main__':
    print(solution("zzz", "zzzz"))