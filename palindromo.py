def verifica_palavra(palavra):
    if len(palavra) < 3:
        return "?"

    if palavra == palavra[::-1]:
        return "S"

    return "N"


# Exemplos de uso
palavra1 = "oi"
palavra2 = "radar"
palavra3 = "python"

resultado1 = verifica_palavra(palavra1)
resultado2 = verifica_palavra(palavra2)
resultado3 = verifica_palavra(palavra3)

print(f"Palavra: {palavra1}, Resultado: {resultado1}")
print(f"Palavra: {palavra2}, Resultado: {resultado2}")
print(f"Palavra: {palavra3}, Resultado: {resultado3}")

#Neste código, a função verifica_palavra recebe uma palavra como parâmetro e realiza as seguintes verificações:

#Se a palavra tem menos de 3 caracteres, retorna "?"
#Se a palavra é um palíndromo (igual quando lida de trás para frente), retorna "S"
#Caso contrário, retorna "N"
#Os exemplos de uso no final do código demonstram como a função pode ser aplicada a diferentes palavras 
#e exibe os resultados de acordo com as regras especificadas.

