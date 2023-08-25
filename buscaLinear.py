def busca_linear(array, elemento):
    for i in range(len(array)):
        if array[i] == elemento:
            return i  # Retorna o índice onde o elemento foi encontrado
    return -1  # Retorna -1 se o elemento não for encontrado

# Exemplo de uso
arr = [3, 7, 1, 9, 5, 2]
elemento_procurado = int(input("Digite o elemento que deseja procurar: "))

indice_encontrado = busca_linear(arr, elemento_procurado)

if indice_encontrado != -1:
    print(f"O elemento {elemento_procurado} foi encontrado no índice {indice_encontrado}.")
else:
    print(f"O elemento {elemento_procurado} não foi encontrado no array.")

#Neste código, a função busca_linear percorre cada elemento no array e verifica se é igual ao elemento procurado. 
#Se encontrar o elemento, retorna o índice onde foi encontrado; caso contrário, retorna -1 para indicar que o elemento não foi encontrado.

#O exemplo de uso solicita ao usuário o elemento que deseja procurar e, em seguida, executa a busca linear no array. 
#Ele exibe se o elemento foi encontrado e em qual índice, ou se não foi encontrado.