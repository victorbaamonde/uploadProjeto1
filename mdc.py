def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

# Solicitar entrada dos números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calcular e exibir o MDC
mdc = calcular_mdc(numero1, numero2)
print("O maior divisor comum entre", numero1, "e", numero2, "é:", mdc)

#Neste código, a função calcular_mdc implementa o algoritmo de Euclides para calcular o maior divisor comum entre dois números. 
#A função usa um loop while para repetidamente aplicar a divisão e troca dos números até que o segundo número se torne zero. 
#O resultado final é o MDC.

#O exemplo de uso solicita dois números ao usuário e, em seguida, calcula e exibe o maior divisor comum entre esses dois números.