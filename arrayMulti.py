def ordena(X):
    X.sort()  # Ordena o array X em ordem alfabética crescente
    return len(X)  # Retorna o número de elementos no array após a ordenação

# Exemplo de uso
array = ["banana", "abacaxi", "laranja", "uva"]
numero_de_elementos = ordena(array)
print(f"Número de elementos após ordenação: {numero_de_elementos}")
print("Array ordenado:", array)

#Neste exemplo, a função ordena recebe um array X, o ordena em ordem alfabética crescente usando o método sort() 
#e, em seguida, retorna o número de elementos no array após a ordenação. 
#O exemplo de uso demonstra como a função pode ser aplicada a um array de strings 
#e exibe o número de elementos após a ordenação e o array ordenado.