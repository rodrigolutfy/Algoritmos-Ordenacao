'''
Como funciona:
    Insere cada elemento na posição correta dentro da parte ordenada da lista.
    Eficiente para listas pequenas ou quase ordenadas.

Vantagens:
    - Excelente para listas pequenas ou quase ordenadas (quase O(n)).
    - Simples de implementar e estável.
    - Ordena in-place, sem necessidade de memória extra.

Desvantagens:
    - Ineficiente para listas grandes (O(n²)).
    - Desempenho pior no caso inversamente ordenado.
    - Pouco adequado para grandes volumes de dados.
'''

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1      
        lista[j + 1] = chave    
        
lista = [5, 1, 4, 2, 8]
insertion_sort(lista)
print(lista)