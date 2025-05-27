'''
Vantagens:
    - Merge Sort possui desempenho garantido de O(n log n), mesmo no pior caso.
    - É um algoritmo estável, ou seja, mantém a ordem original dos elementos iguais.

Desvantagens: 
    - Para listas pequenas, pode ser menos eficiente que algoritmos mais simples como o Insertion Sort.
    - O uso de recursão pode causar estouro de pilha (stack overflow) em linguagens ou sistemas com limite
      baixo de chamadas recursivas.
'''

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

lista = [38, 27, 43, 3, 9, 82, 10]
ordenada = merge_sort(lista)
print(ordenada)