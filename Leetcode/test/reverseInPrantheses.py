def solution(inputString):
    
    stack = [] #stack o pila 
    
    for char in inputString:
        if char == ')': #hasta encontrar el cierre se activa
            temp = [] #lista temporal
            while stack and stack[-1] != '(': # Mientras haya elementos en stack (while stack) y el ultimo element no sea apertura (stack[-1])
                temp.append(stack.pop()) # si se cumple, a temp le añadimos el ultimo element de stack
            stack.pop() # Saliendo del bucle quitamos el de apertura '('
            stack.extend(temp) # añadimos los elementos de temp a stack con el orden invertido
        else:
            stack.append(char) # si no hemos encontrado nada, solo apilamos el element
    inputString = ''.join(stack) # unimos todos los elementos de la pila (stack)
    return inputString # regresamos el string nuevo

if __name__ == '__main__':
    word = 'foo(bar)baz'
    print(solution(word))


