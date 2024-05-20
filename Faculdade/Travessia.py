S, N = map(int, input().split())
sapos = []
for _ in range(S):
    sapos.append(int(input()))
pedras = [0] * N
for sapo in sapos:
    for i in range(0, N, sapo):
        pedras[i] = 1
print(*pedras)
