N = int(input())
utilitarias = list(map(int, input().split()))
utilitarias_acertadas = list(map(int, input().split()))

def calcular_porcentagem_acerto(N, utilitarias, utilitarias_acertadas):
    porcentagens = []
    for i in range(N):
        if utilitarias[i] == 0:
            porcentagens.append(0)
        else:
            porcentagem = (utilitarias_acertadas[i] * 100) // utilitarias[i]
            porcentagens.append(porcentagem)
    return porcentagens


porcentagens_acerto = calcular_porcentagem_acerto(N, utilitarias, utilitarias_acertadas)
print(' '.join(map(str, porcentagens_acerto)))
