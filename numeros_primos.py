def is_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False

    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6

    return True

def encontrar_primos_no_intervalo(inicio, fim):
    primos = []
    for numero in range(max(2, inicio), fim + 1):
        if is_primo(numero):
            primos.append(numero)
    return primos

# Solicitar entrada do intervalo ao usuário
inicio_intervalo = int(input("Digite o início do intervalo: "))
fim_intervalo = int(input("Digite o fim do intervalo: "))

# Encontrar e exibir os números primos no intervalo
primos_no_intervalo = encontrar_primos_no_intervalo(inicio_intervalo, fim_intervalo)
print("Números primos no intervalo de", inicio_intervalo, "a", fim_intervalo, ":", primos_no_intervalo)

#Neste código, a função is_primo verifica se um número é primo usando o Teste de Primalidade de Miller-Rabin. 
#A função encontrar_primos_no_intervalo percorre todos os números no intervalo especificado e verifica se são primos usando a função is_primo.

#O exemplo de uso solicita ao usuário um intervalo e, em seguida, encontra e exibe os números primos dentro desse intervalo.