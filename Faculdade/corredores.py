N = int(input())  
corredores = []

for _ in range(N):
    nome, matricula, tempo = input().split()
    tempo=float(tempo)
    matricula=int(matricula)  
    corredores.append((tempo, nome, matricula))

corredores_ordenados = sorted(corredores,key=lambda x: (x[0], x[1] ))  

for tempo, nome, matricula in corredores_ordenados:
    print(nome, matricula, tempo)  
