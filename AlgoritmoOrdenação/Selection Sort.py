def selection_sort(dados):
    num = len(dados)
    for i in range(len(dados)):
        mini = i
        for j in range(i + 1, len(dados)):
            if dados[j] < dados[mini]:
                mini = j
        dados[i], dados[mini] = dados[mini], dados[i]
    return dados

dados = [1,10,28,5,7,0,3,13,8]
dados_ordenados = selection_sort(dados)
print(dados_ordenados) # [3, 9, 10, 27, 38, 43, 82]
