def busca_binaria_recursiva(lista,alvo,inicio=0,fim=None):
    if fim is None:
        fim = len(lista)-1

    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio

    elif alvo < lista[meio]:
        return busca_binaria_recursiva(lista,alvo,inicio,meio-1)
    else:
        return busca_binaria_recursiva(lista,alvo,meio+1,fim)


numeros = [1, 3, 4, 6, 7, 8, 10, 13, 14]

index = busca_binaria_recursiva(numeros,10)
print(f"O numero 10 esta no indice: {index}")

index_inexistente = busca_binaria_recursiva(numeros,5)
print(f"O numero 5 esta no indice: {index_inexistente}")