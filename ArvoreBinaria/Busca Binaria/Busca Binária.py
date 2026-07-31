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

numeros = [1,2,3,4,5,6,7,8,9,10]
posicao = busca_binaria(numeros,1)

if posicao  != -1:
    print(f"Elemento encontrado: {posicao}")
else:
    print("Elemento nao encontrado")