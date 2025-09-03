def divide_ordena(vetor):
    if len(vetor) <= 1:  # Caso base: já está ordenado
        return vetor

    # Escolhe o elemento do meio como pivô
    pivo = vetor[len(vetor) // 2]

    menores = [x for x in vetor if x < pivo]
    iguais = [x for x in vetor if x == pivo]
    maiores = [x for x in vetor if x > pivo]

    # Ordena recursivamente os menores e maiores
    return divide_ordena(menores) + iguais + divide_ordena(maiores)
  
# ---- Testes ----
valores = [10, 7, 8, 9, 1, 5]
print(divide_ordena(valores))  # [1, 5, 7, 8, 9, 10]

valores = [64, 34, 25, 12, 22, 11, 90]
print(divide_ordena(valores))  # [11, 12, 22, 25, 34, 64, 90]
