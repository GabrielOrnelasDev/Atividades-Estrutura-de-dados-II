#Atividade avaliativa 3

import random
import copy
import sys

sys.setrecursionlimit(10000)


# ---------------------------------------------------------------------------
# 1. BUBBLE SORT
# ---------------------------------------------------------------------------
def bubble_sort(vetor):
    v = vetor.copy()
    n = len(v)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocas += 1
                trocou = True
        if not trocou:
            break

    return v, comparacoes, trocas


# ---------------------------------------------------------------------------
# 2. INSERTION SORT
# ---------------------------------------------------------------------------
def insertion_sort(vetor):
    v = vetor.copy()
    n = len(v)
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, n):
        chave = v[i]
        j = i - 1
        movimentacoes += 1
        while j >= 0:
            comparacoes += 1
            if v[j] > chave:
                v[j + 1] = v[j]
                movimentacoes += 1
                j -= 1
            else:
                break
        v[j + 1] = chave

    return v, comparacoes, movimentacoes


# ---------------------------------------------------------------------------
# 3. SELECTION SORT
# ---------------------------------------------------------------------------
def selection_sort(vetor):
    v = vetor.copy()
    n = len(v)
    comparacoes = 0
    trocas = 0

    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]
            trocas += 1

    return v, comparacoes, trocas


# ---------------------------------------------------------------------------
# 4. QUICK SORT (particionamento de Lomuto, pivô = último elemento)
# ---------------------------------------------------------------------------
def quick_sort(vetor):
    v = vetor.copy()
    contadores = {"comparacoes": 0, "movimentacoes": 0}

    def particiona(v, baixo, alto):
        pivo = v[alto]
        i = baixo - 1
        for j in range(baixo, alto):
            contadores["comparacoes"] += 1
            if v[j] <= pivo:
                i += 1
                v[i], v[j] = v[j], v[i]
                contadores["movimentacoes"] += 1
        v[i + 1], v[alto] = v[alto], v[i + 1]
        contadores["movimentacoes"] += 1
        return i + 1

    def _quick_sort(v, baixo, alto):
        if baixo < alto:
            p = particiona(v, baixo, alto)
            _quick_sort(v, baixo, p - 1)
            _quick_sort(v, p + 1, alto)

    _quick_sort(v, 0, len(v) - 1)
    return v, contadores["comparacoes"], contadores["movimentacoes"]


# ---------------------------------------------------------------------------
# FUNÇÃO AUXILIAR: roda os 4 algoritmos sobre cópias idênticas de um vetor
# ---------------------------------------------------------------------------
def rodar_experimento(vetor_original):
    vetor_bubble = vetor_original.copy()
    vetor_insertion = vetor_original.copy()
    vetor_selection = vetor_original.copy()
    vetor_quick = vetor_original.copy()

    _, comp_b, tro_b = bubble_sort(vetor_bubble)
    _, comp_i, mov_i = insertion_sort(vetor_insertion)
    _, comp_s, tro_s = selection_sort(vetor_selection)
    _, comp_q, mov_q = quick_sort(vetor_quick)

    return {
        "bubble": {"comparacoes": comp_b, "trocas": tro_b},
        "insertion": {"comparacoes": comp_i, "movimentacoes": mov_i},
        "selection": {"comparacoes": comp_s, "trocas": tro_s},
        "quick": {"comparacoes": comp_q, "movimentacoes": mov_q},
    }


def imprime_linha_tabela(tamanho, resultado):
    b = resultado["bubble"]
    i = resultado["insertion"]
    s = resultado["selection"]
    q = resultado["quick"]
    print(f"{tamanho:>7} | "
          f"{b['comparacoes']:>10} | {b['trocas']:>8} | "
          f"{i['comparacoes']:>10} | {i['movimentacoes']:>8} | "
          f"{s['comparacoes']:>10} | {s['trocas']:>8} | "
          f"{q['comparacoes']:>10} | {q['movimentacoes']:>8}")


# ---------------------------------------------------------------------------
# ETAPA 3 - EXPERIMENTO PRINCIPAL (vetores aleatórios de 10, 20 e 1000)
# ---------------------------------------------------------------------------
def experimento_principal(seed=42):
    random.seed(seed)
    tamanhos = [10, 20, 1000]
    resultados = {}

    print("=" * 100)
    print("ETAPA 3 - RESULTADOS (vetores aleatórios)")
    print("=" * 100)
    cabecalho = (f"{'Tam.':>7} | {'BubbleComp':>10} | {'BubbleTro':>8} | "
                 f"{'InsertComp':>10} | {'InsertMov':>8} | "
                 f"{'SelectComp':>10} | {'SelectTro':>8} | "
                 f"{'QuickComp':>10} | {'QuickMov':>8}")
    print(cabecalho)
    print("-" * 100)

    for tamanho in tamanhos:
        vetor_original = [random.randint(1, 100000) for _ in range(tamanho)]
        resultado = rodar_experimento(vetor_original)
        resultados[tamanho] = resultado
        imprime_linha_tabela(tamanho, resultado)

    print("=" * 100)
    return resultados


# ---------------------------------------------------------------------------
# DESAFIO ADICIONAL - aleatório x ordenado x ordem inversa
# ---------------------------------------------------------------------------
def desafio_adicional(tamanho=1000, seed=42):
    random.seed(seed)
    vetor_aleatorio = [random.randint(1, 100000) for _ in range(tamanho)]
    vetor_ordenado = sorted(vetor_aleatorio)
    vetor_invertido = sorted(vetor_aleatorio, reverse=True)

    casos = {
        "Aleatório": vetor_aleatorio,
        "Já ordenado": vetor_ordenado,
        "Ordem inversa": vetor_invertido,
    }

    print()
    print("=" * 100)
    print(f"DESAFIO ADICIONAL - vetores de tamanho {tamanho}")
    print("=" * 100)
    cabecalho = (f"{'Caso':>14} | {'BubbleComp':>10} | {'BubbleTro':>8} | "
                 f"{'InsertComp':>10} | {'InsertMov':>8} | "
                 f"{'SelectComp':>10} | {'SelectTro':>8} | "
                 f"{'QuickComp':>10} | {'QuickMov':>8}")
    print(cabecalho)
    print("-" * 100)

    resultados = {}
    for nome_caso, vetor in casos.items():
        resultado = rodar_experimento(vetor)
        resultados[nome_caso] = resultado
        b = resultado["bubble"]
        i = resultado["insertion"]
        s = resultado["selection"]
        q = resultado["quick"]
        print(f"{nome_caso:>14} | "
              f"{b['comparacoes']:>10} | {b['trocas']:>8} | "
              f"{i['comparacoes']:>10} | {i['movimentacoes']:>8} | "
              f"{s['comparacoes']:>10} | {s['trocas']:>8} | "
              f"{q['comparacoes']:>10} | {q['movimentacoes']:>8}")

    print("=" * 100)
    return resultados


if __name__ == "__main__":
    resultados_principais = experimento_principal(seed=42)
    resultados_desafio = desafio_adicional(tamanho=1000, seed=42)