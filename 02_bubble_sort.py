'''
Vantagens:
    - Funciona bem para listas pequenas ou quase ordenadas
    - Ótimo para aprender conceitos básicos de comparação e troca.
    
Desvantagens:
    - Faz muitas comparações e trocas desnecessárias
    - Mmuito lento para grandes volumes de dados, perdendo para algoritmos mais avançados.
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