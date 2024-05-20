n = int(input())
jogadores = list(map(int, input().split()))

def imprimir_assassinatos(jogadores, assassinatos):
    n = len(jogadores)
    max_assassinatos = max(assassinatos) + 1
    contador = [0] * max_assassinatos
    for i in range(n):
        contador[assassinatos[i]] += 1
    resultado = []
    for i in range(max_assassinatos):
        for _ in range(contador[i]):
            resultado.append(i)
    return resultado

resultado = imprimir_assassinatos(jogadores, jogadores)
print(*resultado)
