def ordem_crescente(vetor):
    ordemCrescente = True
    for i in range(1, len(vetor)):
        if(vetor[i] < vetor[i - 1]):
            return False
    return True

vetor = [1, 2, 3, 4, 6, 5]

if(ordem_crescente(vetor)):
    print("O vetor está em ordem crescente")
else:
    print("O vetor não está em ordem crescente")
