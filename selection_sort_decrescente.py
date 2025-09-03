def selection_sort_decrescente(vetor):
    n = len(vetor)
    for i in range(n - 1):
        # Assume que o maior está na posição i
        max_index = i
        for j in range(i + 1, n):
            if vetor[j] > vetor[max_index]:
                max_index = j
        # Troca o maior encontrado com o da posição i
        vetor[i], vetor[max_index] = vetor[max_index], vetor[i]
      
# ---- Testes ----
valores = [64, 25, 12, 22, 11]
selection_sort_decrescente(valores)
print(valores)  # [64, 25, 22, 12, 11]

valores = [1, 2, 3, 4, 5]
selection_sort_decrescente(valores)
print(valores)  # [5, 4, 3, 2, 1]

valores = [10, 10, 5, 7]
selection_sort_decrescente(valores)
print(valores)  # [10, 10, 7, 5]

valores = []
selection_sort_decrescente(valores)
print(valores)  # []
