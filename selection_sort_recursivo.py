def selection_sort_recursivo(vetor, inicio=0):
    n = len(vetor)

    # Caso base
    if inicio >= n - 1:
        return

    # Encontra o índice do menor elemento no subvetor [inicio..n-1]
    min_index = inicio
    for j in range(inicio + 1, n):
        if vetor[j] < vetor[min_index]:
            min_index = j

    # Troca o menor elemento encontrado com o da posição atual
    vetor[inicio], vetor[min_index] = vetor[min_index], vetor[inicio]

    # Chamada recursiva para o resto do vetor
    selection_sort_recursivo(vetor, inicio + 1)


# ---- Testes ----
valores = [64, 25, 12, 22, 11]
selection_sort_recursivo(valores)
print(valores)  # [11, 12, 22, 25, 64]

valores = [1, 2, 3, 4, 5]
selection_sort_recursivo(valores)
print(valores)  # [1, 2, 3, 4, 5]

valores = [5]
selection_sort_recursivo(valores)
print(valores)  # [5]

valores = []
selection_sort_recursivo(valores)
print(valores)  # []
