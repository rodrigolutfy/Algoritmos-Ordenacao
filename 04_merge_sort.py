'''
Como funciona:
    Divide a lista em partes menores, ordena e funde recursivamente.
    Utiliza o método dividir-para-conquistar com boa eficiência.

Vantagens:
    - Tempo garantido O(n log n) no pior caso.
    - Estável (preserva a ordem relativa dos iguais).
    - Muito eficiente para grandes listas e listas ligadas.

Desvantagens:
    - Usa memória extra proporcional ao tamanho da lista.
    - Implementação mais complexa que os métodos simples.
    - Pode ser mais lento em listas muito pequenas devido à sobrecarga.
'''

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

lista = [38, 27, 43, 3, 9, 82, 10]
ordenada = merge_sort(lista)
print(ordenada)