'''
Como funciona:
    Distribui os dados em baldes e ordena individualmente.
    Funciona bem com dados uniformemente distribuídos.

Vantagens:
    - Muito eficiente para dados uniformemente distribuídos (quase O(n)).
    - Pode ser paralelo facilmente.
    - Estável, dependendo do método de ordenação interno.
    
Desvantagens:
    - Desempenho ruim para dados não uniformemente distribuídos.
    - Complexidade extra para escolher o número e intervalo dos baldes.
    - Usa memória extra para os baldes.
'''

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    num_buckets = 10
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int(num * num_buckets)
        if index == num_buckets:
            index -= 1
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    for i in range(len(arr)):
        arr[i] = sorted_arr[i]

    return arr

lista = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
bucket_sort(lista)
print(lista)