'''
Vantagens: 
    - Muito eficiente na prática, e é o algoritmo de ordenação mais usado em diversas bibliotecas
    - Não requer memória adicional significativa
    
Desvantagens: 
    - Não é estável — pode alterar a ordem de elementos iguais.
    - A versão recursiva simples (como essa) não é a mais eficiente; otimizações são necessárias para casos reais.
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