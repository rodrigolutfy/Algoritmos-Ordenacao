'''
Como funciona:
    Conta a frequência de cada valor e posiciona diretamente.
    Eficiente para dados inteiros pequenos e com pouca variação.

Vantagens:
    - Tempo linear O(n + k) para dados com faixa limitada.
    - Muito eficiente para dados inteiros com valores pequenos.
    - Estável.

Desvantagens:
    - Só funciona para dados inteiros ou discretos com intervalo pequeno.
    - Usa memória extra proporcional ao intervalo dos valores (k).
    - Não é um algoritmo comparativo, limitado a casos específicos.
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