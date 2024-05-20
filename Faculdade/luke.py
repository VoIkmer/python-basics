espaco, teleporte = input().split()
espaco = int(espaco)
teleporte = int(teleporte)
matrix = []
a = 0

for i in range(espaco):
    linhas = [int(z) for z in input().split()]
    matrix.append(linhas)

for r in range(teleporte):
    x, y = input().split()
    x = int(x)
    y = int(y)
    for n in range(espaco):
        if n == y:
            for w in range(x-1, -1, -1):
                if matrix[w][y] == 1:
                    a += 1
                    matrix[w][y] = 0
                    break

print(a)