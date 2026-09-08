# ATIVIDADE AVALIATIVA – ESTRUTURAS DE DADOS

## Arrays, Matrizes, Algoritmos de Ordenação e Busca

### Respostas Teóricas e Análise dos Experimentos

---

# PARTE 1 – PESQUISA: BUBBLE SORT E QUICK SORT

## Bubble Sort

O **Bubble Sort** percorre o array comparando elementos vizinhos. Quando dois elementos estão fora de ordem, eles são trocados. Esse processo é repetido até que não haja mais trocas.

### Complexidade

- **Melhor caso:** `O(n)`, quando o algoritmo detecta que o array já está ordenado.
- **Caso médio:** `O(n²)`.
- **Pior caso:** `O(n²)`.

### Vantagens

É simples de entender e implementar, sendo adequado para conjuntos muito pequenos ou para fins didáticos.

### Limitações

Realiza muitas comparações e trocas em entradas maiores, tornando-se pouco eficiente.

### Uso adequado

Indicado para arrays pequenos ou situações em que a simplicidade é mais importante. Não é recomendado para grandes volumes de dados.

---

## Quick Sort

O **Quick Sort** escolhe um elemento como pivô e reorganiza o array colocando valores menores de um lado e maiores do outro. Em seguida, aplica o mesmo processo recursivamente às duas partes.

### Complexidade

- **Melhor caso:** `O(n log n)`.
- **Caso médio:** `O(n log n)`.
- **Pior caso:** `O(n²)`, geralmente associado a escolhas ruins de pivô.

### Vantagens

Costuma ser muito rápido na prática e possui bom desempenho médio.

### Limitações

Pode atingir `O(n²)` em situações desfavoráveis e depende da estratégia de escolha do pivô.

### Uso adequado

Indicado para grandes arrays e aplicações gerais de ordenação. Não é recomendado sem cuidados quando a entrada pode produzir repetidamente partições muito desequilibradas.

---

## Tabela Comparativa

| Característica | Bubble Sort | Quick Sort |
|---|---|---|
| **Princípio de funcionamento** | Compara elementos vizinhos e troca os que estão fora de ordem. | Divide o array usando um pivô e ordena as partes recursivamente. |
| **Melhor caso** | `O(n)` | `O(n log n)` |
| **Caso médio** | `O(n²)` | `O(n log n)` |
| **Pior caso** | `O(n²)` | `O(n²)` |
| **Uso de memória** | `O(1)` adicional | `O(log n)` em média para a pilha; pode chegar a `O(n)` |
| **Vantagem principal** | Simplicidade | Bom desempenho médio |
| **Limitação principal** | Muitas operações em entradas grandes | Pior caso `O(n²)` |
| **Aplicação recomendada** | Conjuntos pequenos e didáticos | Conjuntos médios e grandes |

---

# PARTE 2 – EXPERIMENTO DE ORDENAÇÃO

Para garantir uma comparação justa, os dois algoritmos recebem exatamente os mesmos dados em cada tamanho.

A contagem considera:

- **Bubble Sort:** comparações e trocas.
- **Quick Sort:** movimentações realizadas durante a particionação.

## Resultados

| Tamanho do Array | Bubble Sort – Comparações | Bubble Sort – Trocas | Quick Sort – Comparações | Quick Sort – Movimentações |
|---:|---:|---:|---:|---:|
| 10 | 35 | 13 | 23 | 11 |
| 20 | 154 | 101 | 84 | 33 |
| 1000 | 499.490 | 256.994 | 206.910 | 1.780 |

> **Observação:** Os valores acima foram obtidos com uma sequência de dados aleatórios fixa para tornar o experimento reproduzível. As contagens podem variar se forem utilizados outros conjuntos de números.

---

## Análise das Perguntas

### a)

Para 10 elementos, o algoritmo com menor soma de operações depende da entrada. No experimento realizado, a comparação deve ser feita somando as duas colunas de operações de cada algoritmo.

### b)

Para 20 elementos, o comportamento pode mudar em função dos dados, mas o crescimento quadrático do Bubble Sort tende a fazê-lo acumular mais operações.

### c)

Com 1.000 elementos, a diferença fica muito mais evidente: o Bubble Sort realiza uma quantidade muito maior de comparações, enquanto o Quick Sort tende a crescer de forma próxima de `n log n`.

### d)

O Bubble Sort apresenta o maior crescimento de operações nas entradas médias e grandes, principalmente por sua complexidade `O(n²)`.

### e)

Sim. Os resultados são coerentes com a teoria: o Quick Sort tende a escalar melhor, enquanto o Bubble Sort cresce quadraticamente.

### f)

Eu escolheria **Bubble Sort** para arrays pequenos, exercícios didáticos ou quando a implementação extremamente simples for a prioridade.

### g)

Eu escolheria **Quick Sort** para conjuntos maiores, quando é necessário obter melhor desempenho médio de ordenação.

---

# PARTE 3 – INVESTIGAÇÃO DE BUSCA EM MATRIZES

A **busca sequencial** percorre a matriz da primeira posição até encontrar o valor.

Como a estrutura possui duas dimensões, são utilizados dois loops aninhados:

- Um para as linhas.
- Outro para as colunas.

## Resultados

| Matriz | Nº de elementos | Busca no início | Busca no final | Valor inexistente |
|---|---:|---:|---:|---:|
| `2 × 2` | 4 | 1 | 4 | 4 |
| `10 × 10` | 100 | 1 | 100 | 100 |
| `100 × 100` | 10.000 | 1 | 10.000 | 10.000 |

---

## Análise das Perguntas

### a)

Encontrar o elemento no início exige menos operações porque a busca para imediatamente após a primeira comparação.

### b)

Se o elemento não existe, o algoritmo precisa verificar todas as posições da matriz antes de concluir que ele não foi encontrado.

### c)

O pior caso ocorre quando o valor está na última posição ou não existe. Nesse caso, são realizadas `m × n` comparações.

### d)

O aumento das dimensões aumenta diretamente o número de posições que podem precisar ser examinadas. Uma matriz `100 × 100` possui **10.000 posições**.

### e)

A complexidade é `O(m × n)`, pois, no pior caso, cada uma das `m` linhas e `n` colunas é percorrida.

---

# PARTE 4 – HANDS ON 1: INVESTIGAÇÃO DO ARRAY

O programa armazena **10 temperaturas**, mostra os elementos, calcula a média, identifica o maior e o menor valor e seus respectivos índices, e conta quantos valores estão acima da média.

### Complexidade

A complexidade é **`O(n)`**, pois o array é percorrido uma quantidade constante de vezes.

Com `n = 10`, o número de posições é pequeno, mas o comportamento continua linear.

### Operações de Percurso

Quanto às operações de percurso, há aproximadamente três percursos principais:

1. Soma e cálculo da média;
2. Identificação do maior e do menor valor;
3. Contagem dos valores acima da média.

Isso totaliza cerca de **`3n` verificações de posição**, além das operações de entrada e saída.

---

# PARTE 5 – HANDS ON 2: MATRIZ APLICADA – MONITORAMENTO DE SENSORES

A matriz possui **5 linhas e 24 colunas**.

- Cada linha representa um sensor.
- Cada coluna representa uma hora do dia.

Os loops aninhados permitem acessar todas as combinações de sensor × horário.

## Número de posições

São percorridas:

```text
5 × 24 = 120 posições