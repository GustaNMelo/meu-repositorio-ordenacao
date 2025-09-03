# Repositório de Exercícios de Ordenação em Python

Este repositório contém a implementação de seis atividades sobre vetores e algoritmos de ordenação em Python.

---

## Atividades

1. **Verificação de ordem crescente**  
   Função que verifica se um vetor de inteiros está em ordem crescente, retornando `True` ou `False`.

2. **Inserção em vetor ordenado**  
   Função que recebe um inteiro e um vetor em ordem crescente, e insere o inteiro na posição correta mantendo a ordem.

3. **Insertion Sort recursivo**  
   Implementação recursiva do algoritmo de ordenação por inserção, ordenando o vetor in-place.

4. **Selection Sort recursivo**  
   Implementação recursiva do algoritmo de ordenação por seleção, ordenando o vetor in-place.

5. **Ordenação decrescente (inspirada em Selection Sort)**  
   Função que permuta os elementos de um vetor para que fiquem em ordem decrescente, usando a lógica do Selection Sort para encontrar o maior elemento a cada passo.

6. **Algoritmo inventado mais rápido**  
   Função chamada **Divide Ordena**, inspirada no Quick Sort.  
   - A ideia foi escolher um elemento central (pivô) e dividir o vetor em três grupos: menores, iguais e maiores que o pivô.  
   - Ordena recursivamente os grupos menores e maiores e combina todos para obter o vetor final ordenado.  
   - Dessa forma, consegui um algoritmo que é **mais rápido que insertion e selection sort**, com complexidade média **O(n log n)**, sem precisar comparar todos os elementos entre si.

---

## Como rodar

Cada exercício está implementado em um arquivo Python separado. Para testar, basta executar o arquivo correspondente, por exemplo:

```bash
python ordem_crescente.py
python insere_ordenado.py
python insertion_sort_recursivo.py
python selection_sort_recursivo.py
python selection_sort_decrescente.py
python divide_ordena.py
