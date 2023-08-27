def busca_binaria(array, elemento):
    inicio = 0
    fim = len(array) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if array[meio] == elemento:
            return meio  # Retorna o índice onde o elemento foi encontrado
        elif array[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return -1  # Retorna -1 se o elemento não for encontrado

# Exemplo de uso
arr_ordenado = [1, 2, 3, 5, 7, 9]
elemento_procurado = int(input("Digite o elemento que deseja procurar: "))

indice_encontrado = busca_binaria(arr_ordenado, elemento_procurado)

if indice_encontrado != -1:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice_encontrado}.")
else:
    print(f"O elemento {elemento_procurado} não foi encontrado no array.")

#Neste código, a função busca_binaria realiza uma busca binária no array ordenado para encontrar o elemento desejado. 
#Ela compara o elemento com o elemento do meio do intervalo atual e ajusta os limites do intervalo com base na comparação.

#O exemplo de uso solicita ao usuário o elemento que deseja procurar e, em seguida, executa a busca binária no array ordenado. 
#Ele exibe se o elemento foi encontrado e em qual índice, ou se não foi encontrado. Lembre-se de que a busca binária só funciona em arrays ordenados.

