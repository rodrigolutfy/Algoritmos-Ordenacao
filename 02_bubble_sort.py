'''
Como funciona:
    Compara e troca pares adjacentes até que a lista esteja ordenada.
    O maior elemento 'borbulha' para o final a cada passagem.

Vantagens:
    - Muito simples de implementar e entender.
    - Detecta facilmente quando a lista já está ordenada (versão otimizada).
    - Ordena in-place, sem necessidade de memória extra.

Desvantagens:
    - Muito lento para listas grandes (O(n²)).
    - Pouco eficiente comparado a outros algoritmos simples.
    - Não é estável na sua forma básica (pode ser adaptado para ser).
'''

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista = [7, 2, 4, 3, 8]
bubble_sort(lista)
print("Lista ordenada:", lista)