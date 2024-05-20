numero = int(input("Digite um número do conjunto dos naturais que deseja encontrar a raiz quadrada:")) 
erro = 0.0000000001
raiz = 0.0

if numero >= 0:
    antecessor = 0
    sucessor = 0

    n = numero

    while n * n > numero:
        n = n / 2
    
    while n * n < numero:
        n += 1

    antecessor = n - 1
    sucessor = n

    while abs((raiz * raiz - numero)) > erro:
        raiz = (antecessor + sucessor) / 2

        if (raiz * raiz < numero):
            antecessor = raiz
        else:
            sucessor = raiz

    print("A raiz de", numero, "é:", raiz)

else:
    print("Esse não é um número natural!")


