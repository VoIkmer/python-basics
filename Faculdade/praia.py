matriz =[]

for _ in range(10):
    linha= [t for t in input().split()]
    matriz.append(linha)

for i in range(10):
    for j in range(10):
        if matriz[i][j] == 't':
            for g in range(j-1, -1, -1):
                if matriz[i][g] == '*':
                    matriz[i][j] = 'p'
                    break
                else:
                    break
            for h in range(j+1, 10):
                if matriz[i][h] == '*':
                    matriz[i][j] = 'p'
                    break
                else:
                    break
            for z in range(i-1, -1, -1):
                if matriz[z][j] == '*':
                    matriz[i][j]  = 'p'
                    break
                else:
                    break
            for v in range(i+1, 10):
                if matriz[v][j] == '*':
                    matriz[i][j] = 'p'
                    break
                else:
                    break

for a in range(10):
    for b in range(10):
        print(matriz[a][b], '', end='')
        if b != 9:
            continue
        print(sep='')