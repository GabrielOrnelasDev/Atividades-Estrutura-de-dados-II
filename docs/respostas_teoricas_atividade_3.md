# Atividade Prática — Análise de Algoritmos de Ordenação
### Central de Distribuição de Pedidos

Todos os números apresentados abaixo foram gerados pela execução real do arquivo `ordenacao_experimento.py` (seed fixa = 42, para reprodutibilidade). Cada tamanho de vetor foi gerado uma única vez e copiado igualmente para os quatro algoritmos, conforme exigido no enunciado.

---

## Etapa 2 — Critério de contagem utilizado

- **Comparação**: toda vez que dois valores do vetor são comparados entre si (ex.: `vetor[j] > vetor[j+1]`), independentemente do resultado ser verdadeiro ou falso.
- **Bubble Sort / Selection Sort — "trocas"**: cada operação de troca (`swap`) completa entre duas posições do vetor conta como **1 troca**.
- **Insertion Sort — "movimentações"**: cada deslocamento de um elemento uma posição à direita dentro do laço interno conta como 1 movimentação; a retirada do elemento-chave da posição original também é contabilizada como 1 movimentação. Não existe "troca" clássica nesse algoritmo, por isso o critério é por deslocamento.
- **Quick Sort — "movimentações"**: toda troca de posição feita durante o particionamento (esquema de Lomuto, pivô = último elemento do subvetor), incluindo a troca final que posiciona o pivô em seu lugar definitivo.

---

## Etapa 3 — Resultados (vetores aleatórios)

| Tamanho | Bubble Comparações | Bubble Trocas | Insertion Comparações | Insertion Mov. | Selection Comparações | Selection Trocas | Quick Comparações | Quick Mov. |
|:---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10    | 45      | 26      | 33      | 35      | 45      | 6    | 29     | 15     |
| 20    | 175     | 87      | 101     | 106     | 190     | 15   | 65     | 41     |
| 1.000 | 498.324 | 243.438 | 244.432 | 244.437 | 499.500 | 990  | 10.218 | 6.231  |

---

## Etapa 4 — Análise dos resultados

**a) Qual algoritmo realizou o menor número de comparações para 10 elementos?**

O **Quick Sort**, com apenas 29 comparações, contra 33 do Insertion Sort e 45 do Bubble Sort e do Selection Sort (empatados). Mesmo em vetores pequenos, a estratégia de particionamento do Quick Sort já reduz o número de comparações necessárias.

**b) Qual algoritmo realizou menos trocas ou movimentações?**

O **Selection Sort**, com apenas 6 trocas para 10 elementos. Isso é esperado, pois o Selection Sort troca elementos **no máximo uma vez por posição** (apenas quando encontra um novo mínimo diferente do elemento atual), enquanto os demais podem trocar/mover elementos várias vezes durante o processo.

**c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?**

Parcialmente. Em ambos os tamanhos o Quick Sort teve o menor número de comparações e o Insertion Sort ficou em segundo lugar. Porém, a ordem entre Bubble e Selection **se inverteu**: em 10 elementos os dois empataram em comparações (45), mas em 20 elementos o Selection Sort (190) já ultrapassou o Bubble Sort (175). Isso ocorre porque o número de comparações do Selection Sort **não depende dos dados**, apenas do tamanho do vetor (sempre n(n-1)/2), enquanto o Bubble Sort pode se beneficiar de otimizações (parar quando não há mais trocas).

**d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?**

Houve um crescimento explosivo para Bubble, Insertion e Selection Sort — todos passaram a realizar centenas de milhares de comparações (próximas de n²/2 ≈ 499.500), confirmando o comportamento quadrático. Já o Quick Sort teve um crescimento muito mais moderado, com apenas 10.218 comparações — cerca de **49 vezes menos** que o Selection Sort no mesmo tamanho — evidenciando a diferença entre complexidade O(n²) e O(n log n) na prática.

**e) Bubble, Insertion e Selection apresentam complexidade O(n²) em situações típicas. Eles apresentaram exatamente a mesma quantidade de operações? Explique.**

Não. Apesar de os três pertencerem à mesma classe de complexidade assintótica O(n²), os valores absolutos obtidos foram diferentes:

- O **Selection Sort** realizou **exatamente** n(n-1)/2 comparações em todos os casos (45, 190 e 499.500 para n = 10, 20 e 1.000), pois ele sempre varre todo o restante do vetor em busca do mínimo, independentemente da ordem dos dados.
- O **Bubble Sort** ficou muito próximo desse valor (498.324 para n = 1.000), mas ligeiramente abaixo, graças à otimização de parada antecipada quando nenhuma troca ocorre em uma passada.
- O **Insertion Sort** teve, de longe, o menor número de comparações entre os três (244.432 para n = 1.000, quase metade do Selection Sort), pois ele interrompe a busca pela posição correta assim que encontra um elemento menor que a chave, não precisando comparar com todo o restante do vetor.

Ou seja: a classe de complexidade (O(n²)) é a mesma, mas a **constante multiplicativa** e a **sensibilidade à ordem dos dados de entrada** diferem entre os três algoritmos.

**f) Qual algoritmo apresentou maior crescimento no número de operações?**

Em termos absolutos, **Selection Sort e Bubble Sort** apresentaram o maior crescimento, seguindo fielmente a curva quadrática: quando o tamanho do vetor foi multiplicado por 100 (de 10 para 1.000), o número de comparações do Selection Sort foi multiplicado por **≈ 11.100 vezes** (45 → 499.500), praticamente o valor teórico esperado de 100² = 10.000 vezes. O Insertion Sort cresceu um pouco menos (≈ 7.400 vezes) por causa das interrupções antecipadas.

**g) Como o comportamento experimental do Quick Sort se diferenciou dos demais?**

O Quick Sort cresceu de forma muito mais lenta: de 29 para 10.218 comparações, um fator de **≈ 352 vezes** (bem próximo do esperado para O(n log n), que seria algo como 100 · log(1000)/log(10) ≈ 300), muito distante do fator ≈ 10.000 dos algoritmos quadráticos. Isso mostra na prática a vantagem do particionamento "dividir para conquistar" sobre os métodos de comparação/troca direta par a par.

**h) Os resultados são coerentes com as complexidades teóricas estudadas?**

Sim. Bubble Sort, Insertion Sort e Selection Sort cresceram de forma aproximadamente quadrática (O(n²)), como previsto pela teoria para o caso médio/pior caso. O Quick Sort, por sua vez, cresceu de forma muito mais lenta no cenário aleatório, compatível com O(n log n). O experimento também confirmou (ver Desafio Adicional) que o Quick Sort com pivô fixo pode degenerar para O(n²) em entradas já ordenadas — exatamente o pior caso teórico descrito na literatura.

**i) Qual algoritmo você escolheria para ordenar milhares de pedidos na central de distribuição? Justifique.**

Escolheria o **Quick Sort**. No experimento com 1.000 elementos aleatórios, ele precisou de apenas 10.218 comparações contra cerca de 500.000 dos demais algoritmos — uma diferença que só tende a aumentar conforme o volume de pedidos cresce (milhares ou dezenas de milhares por dia). A única ressalva prática, mostrada no desafio adicional, é o risco de degradação quando os dados já chegam ordenados (ou quase ordenados); para mitigar isso, na implementação real usaria uma escolha de pivô aleatória (ou mediana de três) em vez de sempre o último elemento, garantindo desempenho O(n log n) esperado mesmo em cenários adversos.

---

## Desafio Adicional — Aleatório × Já ordenado × Ordem inversa

Vetor de 1.000 elementos, mesma semente (seed = 42), comparando as três organizações iniciais:

| Caso           | Bubble Comp. | Bubble Trocas | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Trocas | Quick Comp. | Quick Mov. |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| Aleatório      | 499.329 | 241.624 | 242.617 | 242.623 | 499.500 | 990 | 10.695  | 6.335   |
| Já ordenado    | 999     | 0       | 999     | 999     | 499.500 | 0   | 499.500 | 500.499 |
| Ordem inversa  | 499.500 | 499.494 | 499.500 | 500.493 | 499.500 | 502 | 497.440 | 249.465 |

### Análise

**A organização inicial dos dados interfere na quantidade de operações realizadas por todos os algoritmos da mesma maneira? Não.** Cada algoritmo reage de forma bem diferente à ordem inicial:

- **Bubble Sort**: é extremamente sensível à ordem inicial. Com o vetor já ordenado, precisou de apenas 999 comparações e **0 trocas** (melhor caso, O(n), graças à otimização de parada antecipada). Já com o vetor invertido, foi ao pior caso, com quase 500 mil comparações **e** quase 500 mil trocas — o pior desempenho entre os três casos.

- **Insertion Sort**: também muito sensível. Vetor já ordenado é o melhor caso possível (999 comparações, o mínimo teórico de n-1), enquanto o vetor invertido é o pior caso (499.500 comparações, o máximo teórico de n(n-1)/2). Reproduz de forma quase perfeita os limites teóricos O(n) e O(n²).

- **Selection Sort**: é o algoritmo **menos sensível à ordem inicial em termos de comparações** — permaneceu fixo em 499.500 comparações nos três cenários, pois sempre percorre todo o restante do vetor procurando o mínimo, não importa a ordem. Apenas o número de **trocas** varia (0 no vetor ordenado, 502 no invertido, 990 no aleatório), mas isso pouco influencia o custo total, já que trocas são muito mais raras que comparações.

- **Quick Sort (pivô = último elemento)**: apresenta o comportamento **oposto** ao dos outros três. Ele é o mais rápido no caso aleatório (10.695 comparações) e o **pior** exatamente nos casos "organizados" (já ordenado ou invertido), chegando a quase 500 mil comparações — seu pior caso teórico O(n²). Isso acontece porque, ao escolher sempre o último elemento como pivô, um vetor já ordenado gera partições completamente desbalanceadas (um lado sempre vazio), degenerando a recursão em uma sequência linear de n chamadas, cada uma processando um elemento a menos — o comportamento típico do pior caso do Quick Sort.