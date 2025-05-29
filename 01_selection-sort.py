'''
Como funciona:
    Seleciona o menor elemento e o coloca na posição correta em cada iteração.
    Divide a lista em parte ordenada e não ordenada.

Vantagens:
    - Simples de entender e implementar.
    - Consome pouca memória extra (in-place).
    - Previsível em tempo de execução (sempre O(n²))

Desvantagens:
    - Ineficiente para listas grandes (tempo quadrático).
    - Não é estável (a ordem relativa dos iguais pode mudar).
    - Desempenho não melhora para listas quase ordenadas.
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