def margesort(lista):
    if len(lista) <= 1:
        return lista

    middle = len(lista) // 2
    esquerda = lista[:middle]
    direita = lista[middle:]

    # 3. Recursão: Mandar cortar as metades até virarem listas de 1 elemento
    sortear_esquerda = margesort(esquerda)
    sortear_direita = margesort(direita)
    
    # 4. Juntar as duas metades já organizadas usando a função merge!
    return marge(sortear_esquerda,sortear_direita)

def marge(lefth, righth):
    resultado = []
    i = j = 0

    while i < len(lefth) and j < len(righth):
        if lefth[i] <= righth[j]:
            resultado.append(lefth[i])
            i += 1
        else:
            resultado.append(righth[j])
            j += 1

    resultado.extend(lefth[i:])
    resultado.extend(righth[j:])
    return resultado

dados = [1,10,28,5,7,0,3,13,8]
dados_ordenados = margesort(dados)
print(dados_ordenados) # [3, 9, 10, 27, 38, 43, 82]