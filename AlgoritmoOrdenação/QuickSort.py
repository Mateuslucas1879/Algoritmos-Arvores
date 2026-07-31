def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr)//2]

    esquerda = [x for x in arr if x < pivo]
    medio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]

    return quicksort(esquerda) + medio + quicksort(direita)

dados = [7, 2, 1, 6, 8, 5, 3, 4]
dados_ordenacao = quicksort(dados)
print(dados_ordenacao)