'''
Vantagens:
    - Eficiente para listas pequenas ou quase ordenadas
    - Baixa movimentação de dados

Desvantagens:
    - Pouco eficiente com grandes volumes de dados 
    - Lento para listas grandes 
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