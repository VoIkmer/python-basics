n = int(input())  

corredores = []
for _ in range(n):
    nome, matricula, tempo = input().split()  
    corredores.append((float(tempo), nome, int(matricula)))

corredores_ordenados = sorted(corredores)

for tempo, nome, matricula in corredores_ordenados:
    print(nome, matricula, tempo)  
