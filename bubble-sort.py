def bubble_sort(arr):
    n = len(arr)
    # Percorre todos os elementos da lista
    for i in range(n):
        # Últimos i elementos já estão no lugar correto
        for j in range(0, n - i - 1):
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Exemplo de uso
lista = [5, 1, 4, 2, 8]
bubble_sort(lista)
print("Lista ordenada:", lista)