# 🚀 Algoritmos de Ordenação & Árvore Binária

Repositório dedicado ao estudo e documentação dos principais algoritmos de ordenação e estruturas de dados em ciência da computação.

---

## 📌 Algoritmos de Ordenação

### 1. QuickSort

Criado em 1959 por **Tony Hoare**, o QuickSort é um dos algoritmos de ordenação por comparação mais famosos e eficientes. Ele serve como base para diversas funções de ordenação padrão em linguagens modernas (como o `std::sort` do C/C++).

#### 🛠️ Funcionamento (Dividir e Conquistar)
O algoritmo baseia-se em colocar um elemento por vez em sua posição correta, reorganizando os demais ao seu redor. Esse elemento especial é chamado de **Pivô**.

1. **Escolher o Pivô:** Seleciona-se um elemento qualquer da lista.
2. **Particionar (Dividir):** Reorganiza-se a lista de modo que:
   - Elementos **menores** que o pivô fiquem à sua esquerda.
   - Elementos **maiores** que o pivô fiquem à sua direita.
   *(Neste ponto, o pivô já se encontra em sua posição final definitiva).*
3. **Recursão (Conquistar):** Aplica-se o mesmo processo de forma independente nas sublistas da esquerda e da direita.

#### 📊 Análise de Complexidade Assintótica
A eficiência do QuickSort depende diretamente da escolha do pivô:

| Cenário | Complexidade de Tempo | O que acontece |
| :--- | :--- | :--- |
| **Melhor Caso** | $O(n \log n)$ | O pivô sempre divide o array exatamente ao meio. |
| **Caso Médio** | $O(n \log n)$ | O pivô divide o array de forma equilibrada na maioria das vezes. |
| **Pior Caso** | $O(n^2)$ | O pivô é sempre o maior ou o menor elemento (ex: escolher o último elemento de uma lista já ordenada). |

---

### 2. MergeSort

Criado pelo matemático **John von Neumann** em 1945, o MergeSort é um exemplo clássico da aplicação rigorosa do paradigma **Dividir e Conquistar**.

#### 🛠️ Funcionamento
O algoritmo opera estritamente em 3 passos recursivos:

1. **Dividir:** Encontra o meio da lista e a divide em duas metades (esquerda e direita).
2. **Conquistar:** Aplica o MergeSort recursivamente em cada metade até atingir o caso base (uma lista com 1 elemento ou vazia, que por definição já está ordenada).
3. **Intercalar (Merge):** Combina (*merge*) as duas sublistas ordenadas em uma única lista maior, garantindo a ordenação correta durante a fusão.

---

### 3. BubbleSort (Ordenação por Bolha)

O Bubble Sort é um dos algoritmos de ordenação mais simples e intuitivos. Ele trabalha de forma local e sequencial flutuando os maiores elementos para o final da lista.

#### 🛠️ Funcionamento
1. Percorre a lista da esquerda para a direita.
2. Compara dois elementos vizinhos por vez (`arr[i]` e `arr[i+1]`).
3. Se o elemento da esquerda for maior que o da direita, realiza a troca.
4. Repete o processo em passadas sucessivas até que nenhuma troca seja necessária.

---

### 4. InsertionSort (Ordenação por Inserção)

O InsertionSort funciona de maneira análoga à forma como organizamos cartas de um baralho na mão: conforme recebemos uma nova carta, varremos a mão e a inserimos no lugar correto.

#### 🛠️ Funcionamento
O algoritmo divide o array mentalmente em duas partes: uma **sublista ordenada** à esquerda e uma **sublista não ordenada** à direita.

1. Inicia a avaliação a partir do segundo elemento (índice 1).
2. Compara o elemento atual com os anteriores (da direita para a esquerda na parte ordenada).
3. Desloca os elementos maiores para a direita para abrir espaço.
4. Insere o elemento em sua posição correta.

---

## 🌲 Árvore Binária

## 🔍 Algoritmos de Busca

### 1. Busca Binária (Binary Search)

A **Busca Binária** é um dos algoritmos de busca mais eficientes da computação. Ela segue a estratégia de divisão pela metade a cada etapa.

> ⚠️ **Pré-condição Obrigatória:** A lista/array **PRECISA estar previamente ordenada**. Caso contrário, o algoritmo não funcionará corretamente.

---

#### 🛠️ Funcionamento na Prática

Considere uma lista ordenada de exemplo onde buscamos o número **10**:

$$arr = [1, 3, 4, 5, 7, 8, 10, 13, 14]$$

* **Passo 1:**
  * Limites: `inicio = 0`, `fim = 8`
  * Cálculo do meio: $meio = \lfloor(0 + 8) / 2\rfloor = 4 \implies arr[4] = 7$
  * Como $10 > 7$, descartamos toda a metade esquerda.
  * Atualização: `inicio = meio + 1` (índice 5).

* **Passo 2:**
  * Sublista considerada: $[8, 10, 13, 14]$ (índices 5 a 8)
  * Cálculo do meio: $meio = \lfloor(5 + 8) / 2\rfloor = 6 \implies arr[6] = 10$
  * **Resultado:** Encontrado! O número **10** está localizado no **índice 6**.

---

#### 📊 Análise de Complexidade Assintótica

| Cenário | Complexidade de Tempo | Descrição |
| :--- | :--- | :--- |
| **Melhor Caso** | $O(1)$ | O elemento buscado está exatamente no meio na primeira tentativa. |
| **Caso Médio** | $O(\log n)$ | O espaço de busca é dividido pela metade a cada iteração. |
| **Pior Caso** | $O(\log n)$ | O elemento está nas extremidades ou não existe na lista. |
| **Espaço** | $O(1)$ | Versão iterativa (não consome memória adicional). |


## 🌲 Árvore Binária de Busca Auto-Balanceada (Árvore AVL)

A **Árvore AVL** é uma Árvore Binária de Busca (BST) que mantém sua altura rigidamente balanceada através do cálculo do **Fator de Balanceamento (FB)** em cada nó.

$$FB = \text{Altura}(\text{Esquerda}) - \text{Altura}(\text{Direita})$$

Para que a árvore continue balanceada, o valor de $FB$ de todos os nós deve ser mantido estritamente em **$\{-1, 0, +1\}$**.

### 🔄 Operações de Rotação
Sempre que uma inserção ou remoção resulta em $FB = \pm 2$, realiza-se uma readequação em tempo $O(1)$:

1. **Rotação Simples à Direita:** Usada quando o desbalanceamento ocorre na subárvore esquerda de um filho esquerdo.
2. **Rotação Simples à Esquerda:** Usada quando o desbalanceamento ocorre na subárvore direita de um filho direito.
3. **Rotação Dupla Esquerda-Direita:** Usada em casos de zig-zag (filho esquerdo, subárvore direita).
4. **Rotação Dupla Direita-Esquerda:** Usada em casos de zig-zag (filho direito, subárvore esquerda).

### 📊 Complexidade
Graças ao balanceamento estrito, o pior caso para qualquer busca, inserção ou remoção é garantido em **$O(\log n)$**.