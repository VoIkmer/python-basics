tabuleiro=[]
contador = 0

for _ in range(8):
    linha=[int(a) for a in input().split()]
    tabuleiro.append(linha)

x,y = input().split()
x=int(x)
y=int(y)

if 0 <= x < 8 and 0 <= y < 8:
    for i in range(x - 1, -1, -1):
        if tabuleiro[i][y] == 2:
            contador += 1
            break
        elif tabuleiro[i][y] ==1:
            break
    
    for i in range(x+1,8):
        if tabuleiro[i][y] ==2:
            contador +=1
            break
        elif tabuleiro[i][y] ==1:
            break

    for j in range(y -1, -1, -1):
        if tabuleiro[x][j] ==2:
            contador +=1
            break
        elif tabuleiro[x][j]:
            break

    for j in range(y+1, 8):
        if tabuleiro[x][j]==2:
            contador +=1
            break
        elif tabuleiro[x][j]==1:
            break

print(contador)



    

