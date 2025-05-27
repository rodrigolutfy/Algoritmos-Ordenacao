'''
Vantagens: 
    - Extremamente rápido — complexidade O(n + k), onde k é o maior valor da lista.
    - Estável (se implementado corretamente), preservando a ordem de elementos iguais.

Desvantagens: 
    - Ineficiente para listas com valores muito altos ou grande faixa de valores.
    - Não é um algoritmo in-place, pois usa arrays auxiliares para contagem.
'''

def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    contagem = [0] * (max_val + 1)
    for num in arr:
        contagem[num] += 1
    i = 0
    for num, freq in enumerate(contagem):
        for _ in range(freq):
            arr[i] = num
            i += 1
    return arr

lista = [4, 2, 2, 8, 3, 3, 1]
counting_sort(lista)
print(lista)