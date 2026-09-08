import random


# ============================================================
# PARTE 2 – EXPERIMENTO DE ORDENAÇÃO
# ============================================================

def bubble_sort(arr):
    arr = arr.copy()
    comparacoes = 0
    trocas = 0

    for i in range(len(arr) - 1):
        trocou = False

        for j in range(len(arr) - 1 - i):
            comparacoes += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
                trocou = True

        if not trocou:
            break

    return arr, comparacoes, trocas


def quick_sort(arr):
    arr = arr.copy()
    comparacoes = 0
    movimentacoes = 0

    def particionar(inicio, fim):
        nonlocal comparacoes, movimentacoes

        pivo = arr[fim]
        i = inicio - 1

        for j in range(inicio, fim):
            comparacoes += 1

            if arr[j] <= pivo:
                i += 1

                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    movimentacoes += 1

        if i + 1 != fim:
            arr[i + 1], arr[fim] = arr[fim], arr[i + 1]
            movimentacoes += 1

        return i + 1

    def ordenar(inicio, fim):
        if inicio < fim:
            posicao_pivo = particionar(inicio, fim)

            ordenar(inicio, posicao_pivo - 1)
            ordenar(posicao_pivo + 1, fim)

    ordenar(0, len(arr) - 1)

    return arr, comparacoes, movimentacoes


# Execução do experimento de ordenação

random.seed(2026)

for tamanho in [10, 20, 1000]:
    dados = [random.randint(0, 9999) for _ in range(tamanho)]

    _, bubble_comparacoes, bubble_trocas = bubble_sort(dados)
    _, quick_comparacoes, quick_movimentacoes = quick_sort(dados)

    print(f"\nTamanho: {tamanho}")
    print("Bubble Sort - Comparações:", bubble_comparacoes)
    print("Bubble Sort - Trocas:", bubble_trocas)
    print("Quick Sort - Comparações:", quick_comparacoes)
    print("Quick Sort - Movimentações:", quick_movimentacoes)


# ============================================================
# PARTE 3 – BUSCA SEQUENCIAL EM MATRIZES
# ============================================================

def busca_matriz(matriz, valor):
    comparacoes = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            comparacoes += 1

            if matriz[i][j] == valor:
                return True, i, j, comparacoes

    return False, -1, -1, comparacoes


def criar_matriz(tamanho):
    matriz = []

    for i in range(tamanho):
        linha = []

        for j in range(tamanho):
            linha.append(i * tamanho + j + 1)

        matriz.append(linha)

    return matriz


# Execução da busca nas matrizes

for tamanho in [2, 10, 100]:
    matriz = criar_matriz(tamanho)

    inicio = matriz[0][0]
    final = matriz[tamanho - 1][tamanho - 1]
    inexistente = -1

    casos = [
        ("Início", inicio),
        ("Final", final),
        ("Inexistente", inexistente)
    ]

    print(f"\nMatriz {tamanho} x {tamanho}")

    for nome, valor in casos:
        encontrado, linha, coluna, comparacoes = busca_matriz(
            matriz, valor
        )

        print(f"{nome}:")
        print("Encontrado:", encontrado)
        print("Linha:", linha)
        print("Coluna:", coluna)
        print("Comparações:", comparacoes)


# ============================================================
# PARTE 4 – HANDS ON 1: ARRAY DE TEMPERATURAS
# ============================================================

temperaturas = []

for i in range(10):
    temperatura = float(
        input(f"Digite a temperatura {i}: ")
    )

    temperaturas.append(temperatura)


media = sum(temperaturas) / len(temperaturas)

maior = temperaturas[0]
menor = temperaturas[0]

indice_maior = 0
indice_menor = 0


for i in range(1, len(temperaturas)):
    if temperaturas[i] > maior:
        maior = temperaturas[i]
        indice_maior = i

    if temperaturas[i] < menor:
        menor = temperaturas[i]
        indice_menor = i


acima_media = 0

for temperatura in temperaturas:
    if temperatura > media:
        acima_media += 1


print("\nTemperaturas armazenadas:")

for i in range(len(temperaturas)):
    print(f"Índice {i}: {temperaturas[i]:.2f} °C")


print(f"\nMédia: {media:.2f} °C")
print(f"Maior temperatura: {maior:.2f} °C")
print(f"Índice do maior valor: {indice_maior}")
print(f"Menor temperatura: {menor:.2f} °C")
print(f"Índice do menor valor: {indice_menor}")
print(f"Valores acima da média: {acima_media}")

print("\nComplexidade: O(n)")
print("Percursos principais realizados: aproximadamente 3n.")


# ============================================================
# PARTE 5 – HANDS ON 2: MONITORAMENTO DE SENSORES
# ============================================================

sensores = []

for i in range(5):
    linha = []

    for j in range(24):
        temperatura = float(
            input(f"Sensor {i} - Hora {j}: ")
        )

        linha.append(temperatura)

    sensores.append(linha)


# 1. Média de cada sensor

medias_sensores = []

for i in range(5):
    soma = 0

    for j in range(24):
        soma += sensores[i][j]

    media = soma / 24
    medias_sensores.append(media)


# 2, 3 e 4. Maior temperatura, sensor e horário

maior = sensores[0][0]
sensor_maior = 0
horario_maior = 0


for i in range(5):
    for j in range(24):
        if sensores[i][j] > maior:
            maior = sensores[i][j]
            sensor_maior = i
            horario_maior = j


# 5. Média geral

soma_geral = 0

for i in range(5):
    for j in range(24):
        soma_geral += sensores[i][j]


media_geral = soma_geral / 120


# 6. Leituras acima de um limite

limite = float(
    input("\nInforme o limite de temperatura: ")
)

acima_limite = 0

for i in range(5):
    for j in range(24):
        if sensores[i][j] > limite:
            acima_limite += 1


# Resultados

print("\n--- RESULTADOS ---")

for i in range(5):
    print(
        f"Média do sensor {i}: "
        f"{medias_sensores[i]:.2f} °C"
    )


print(f"Maior temperatura: {maior:.2f} °C")
print(f"Sensor responsável: {sensor_maior}")
print(f"Horário da ocorrência: {horario_maior}h")
print(f"Média geral: {media_geral:.2f} °C")

print(
    "Leituras acima do limite:",
    acima_limite
)

print("\nQuantidade de posições da matriz: 5 x 24 = 120")
print("Complexidade dos percursos: O(5 x 24) = O(120)")