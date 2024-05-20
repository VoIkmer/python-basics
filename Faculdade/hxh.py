n = int(input())  
aprovados = []

for _ in range(n):
    numero, nome = input().split() 
    aprovados.append((nome, int(numero)))

aprovados_em_ordem = sorted(aprovados)  

for nome, numero in aprovados_em_ordem:
    print(nome, numero)  
