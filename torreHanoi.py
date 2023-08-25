def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 da torre {origem} para a torre {destino}")
        return
    torre_de_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} da torre {origem} para a torre {destino}")
    torre_de_hanoi(n-1, auxiliar, destino, origem)

# Exemplo de uso
numero_de_discos = int(input("Digite o número de discos: "))
torre_de_hanoi(numero_de_discos, 'A', 'C', 'B')

#Neste código, a função torre_de_hanoi é implementada usando a técnica de recursão. 
#Ela recebe o número de discos, a torre de origem ('A'), a torre de destino ('C') e a torre auxiliar ('B'). 
#A função move os discos usando a abordagem clássica da Torre de Hanói.

#O exemplo de uso solicita ao usuário o número de discos 
#e, em seguida, chama a função torre_de_hanoi para resolver o problema da Torre de Hanói para esse número de discos, 
#movendo os discos da torre A para a torre C com a ajuda da torre B.





