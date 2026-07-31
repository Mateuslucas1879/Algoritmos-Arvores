def bubblesort(lista):
    num = len(lista)
    for i in range(num):
        swapped = False
        for j in range(0,num - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True

        if not swapped:
            break
    return lista

# Exemplo de uso:
dados = [10,13,70,5, 1, 4, 2]
print(bubblesort(dados))  # Output: [1, 2, 4, 5]