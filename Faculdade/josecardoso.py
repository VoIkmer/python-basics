n = int(input())  
lista = []

for _ in range(n):
    musica = input()  
    lista.append(musica)

lista_ordenadas = sorted(lista) 

for musica in lista_ordenadas:
    print(musica)  
