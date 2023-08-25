for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#Neste código, usamos um loop for para percorrer números de 1 a 100. 
#Para cada número, verificamos se é um múltiplo de 3 e/ou 5 e imprimimos "Fizz", "Buzz" ou "FizzBuzz" conforme apropriado. 
#Se não for múltiplo de nenhum, apenas imprimimos o próprio número.