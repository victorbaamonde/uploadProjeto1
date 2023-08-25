def insertion_sort(array):
    for i in range(1, len(array)):
        chave = array[i]
        j = i - 1
        while j >= 0 and chave < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = chave

# Exemplo de uso
arr_insertion = [12, 11, 13, 5, 6]
insertion_sort(arr_insertion)
print("Insertion Sort:", arr_insertion)

#Neste código, a função insertion_sort implementa o algoritmo de ordenação por inserção. 
#Ela percorre o array da esquerda para a direita, inserindo cada elemento em sua posição correta entre os elementos anteriores já ordenados.

#O exemplo de uso demonstra como a função insertion_sort pode ser aplicada a um array e exibe o array ordenado.