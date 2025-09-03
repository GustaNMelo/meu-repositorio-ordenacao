def insere_ordenado(x, vetor):
    for i in range(len(vetor)):
        if(x < vetor[i]):
            vetor.insert(i, x)
            return vetor
        # Se não encontrou posíção, insere no final
    vetor.append(x)
    return vetor
    
vetor = [1, 2, 3, 4, 6]
x = 5
print("Vetor original: ", vetor)
insere_ordenado(x, vetor)
print("Vetor com novo valor: ", vetor)
