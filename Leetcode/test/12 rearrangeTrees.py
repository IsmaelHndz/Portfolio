def rearrange (lista_de_personas):
    """sumary_line
    
    Keyword arguments: a = [-1, 150, 190, 170, -1, -1, 160, 180] ->>> [-1, 150, 160, 170, -1, -1, 180, 190]
    argument -- Sort without move the trees (-1)
    Return: return sorted list
    """
    estaturas = list(filter(lambda x: x != -1, lista_de_personas))
    estaturas.sort()
    count = 0
    for i in range(len(lista_de_personas)):
        if lista_de_personas[i] != -1:
            lista_de_personas[i] = estaturas[count]
            count += 1

    
    
    return lista_de_personas


if __name__ == '__main__':
    print(rearrange([-1, 150, 190, 170, -1, -1, 160, 180]))