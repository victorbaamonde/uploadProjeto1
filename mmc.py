def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def calcular_mmc(a, b):
    return (a * b) // calcular_mdc(a, b)

# Solicitar entrada dos números ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Calcular e exibir o MMC
mmc = calcular_mmc(numero1, numero2)
print("O mínimo múltiplo comum entre", numero1, "e", numero2, "é:", mmc)

#Neste código, a função calcular_mmc utiliza a relação entre o MDC (maior divisor comum) e o MMC (mínimo múltiplo comum): 
#MMC(a, b) = (a * b) / MDC(a, b). 
#A função calcular_mdc é usada para calcular o MDC entre os dois números, que é então usado para calcular o MMC.

#O exemplo de uso solicita dois números ao usuário e, em seguida, calcula e exibe o mínimo múltiplo comum entre esses dois números.