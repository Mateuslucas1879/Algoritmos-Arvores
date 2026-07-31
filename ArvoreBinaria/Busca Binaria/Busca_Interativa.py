def busca_binaria(lista,alvo):
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] > alvo:
            fim = meio - 1
        else:
            inicio = meio + 1
    return -1

numeros = [1, 3, 4, 6, 7, 8, 10, 13, 14]
posicao = busca_binaria(numeros,10)

if posicao != -1:
    print(f"Elemento encontrado no índice {posicao}")
else:
    print("Elemento não encontrado")