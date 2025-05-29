'''
Como funciona:
    Escolhe um pivô e particiona os elementos em menores e maiores.
    Ordena recursivamente as partições com boa eficiência média.

Vantagens:
    - Muito rápido na média (O(n log n)).
    - Ordenação in-place (usa pouca memória extra).
    - Bom desempenho prático na maioria dos casos.

Desvantagens:
    - Pior caso O(n²), quando o pivô é mal escolhido.
    - Não é estável.
    - Implementação recursiva pode causar estouro de pilha em listas grandes.
'''

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[0]
        menores = [x for x in lista[1:] if x <= pivo]
        maiores = [x for x in lista[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

lista = [10, 5, 2, 3, 7, 6, 4]
ordenada = quick_sort(lista)
print(ordenada)