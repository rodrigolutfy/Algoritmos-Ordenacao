'''
Vantagens: 
    - Complexidade linear O(nk) em muitos casos, onde k é o número de dígitos.
    - Muito eficiente para listas grandes de inteiros com tamanhos de dígito semelhantes.

Desvantagens: 
    - Requer que os números sejam inteiros e positivos (ou adaptação para negativos).
    - Usa memória extra (não é in-place) por causa dos arrays auxiliares.
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