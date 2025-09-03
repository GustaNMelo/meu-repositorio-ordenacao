def insertion_sort_recursivo(vetor, n = None):
    if n is None:
        n = len(vetor)

    # Caso base
    if n <= 1:
        return

    # Ordena os primeiros n - 1 elementos
    insertion_sort_recursivo(vetor, n - 1)

    # Insere o último elemento na posição correta
    ultimo = vetor[n - 1]
    j = n - 2
    while j >= 0 and vetor[j] > ultimo:
        vetor[j + 1] = vetor[j]
        j -= 1
    vetor[j + 1] = ultimo


# ---- Testes ----
valores = [5, 2, 4, 6, 1, 3]
insertion_sort_recursivo(valores)
print(valores)  # [1, 2, 3, 4, 5, 6]

valores = [1, 2, 3, 4, 5]
insertion_sort_recursivo(valores)
print(valores)  # [1, 2, 3, 4, 5]

valores = [9]
insertion_sort_recursivo(valores)
print(valores)  # [9]

valores = []
insertion_sort_recursivo(valores)
print(valores)  # []
