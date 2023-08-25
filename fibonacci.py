def fibonacci_series(n):
    fib_series = [0, 1]
    
    while fib_series[-1] + fib_series[-2] <= n:
        next_fib = fib_series[-1] + fib_series[-2]
        fib_series.append(next_fib)
    
    return fib_series

# Exemplo de uso
numero_limite = int(input("Digite um número limite: "))
serie_fibonacci = fibonacci_series(numero_limite)
print("Série de Fibonacci até", numero_limite, ":", serie_fibonacci)

#Neste código, a função fibonacci_series gera a série de Fibonacci até um determinado número n. 
#Ela inicia com os primeiros dois termos (0 e 1) e, em seguida, gera os termos subsequentes somando os dois últimos termos da série. 
#O loop continua até que o próximo termo gerado exceda o número limite especificado n.

#O exemplo de uso permite ao usuário digitar um número limite e, em seguida, exibe a série de Fibonacci até esse número.