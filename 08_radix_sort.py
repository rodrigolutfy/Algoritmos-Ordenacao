'''
Como funciona:
    Ordena dígito a dígito usando algoritmo estável como apoio.
    Ideal para inteiros ou strings com tamanho fixo.

Vantagens:
    - Pode ordenar números grandes em tempo linear (O(d(n + k)), com d dígitos).
    - Boa opção para strings ou números com tamanho fixo.
    - Estável.

Desvantagens:
    - Depende de um algoritmo estável para ordenar dígitos.
    - Não funciona bem para dados com tamanho variável ou grande número de dígitos.
    - Consome memória extra.
'''

def counting_sort_por_digito(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_por_digito(arr, exp)
        exp *= 10

lista = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(lista)
print(lista)