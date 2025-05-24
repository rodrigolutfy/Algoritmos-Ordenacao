'''
Vantagens:
    - Poucas trocas de posição (eficiente para gravação em memória limitada)
    - Fácil de entender e implementar

Desvantagens:
    - O Selection Sort sempre faz o mesmo número de comparações, mesmo se a lista já estiver ordenada.
    - Não é estável (pode mudar a ordem de elementos iguais)
'''

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]

lista = [64, 25, 12, 22, 11]
selection_sort(lista)
print("Lista ordenada:", lista)