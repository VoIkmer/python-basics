caixas = int(input())
esmeraldas = list(map(int, input().split()))
esmeralda_caos = int(input())

def encontrar_esmeralda(caixas, esmeraldas, esmeralda_caos):
    if esmeralda_caos in esmeraldas:
        return esmeralda_caos
    else:
        return -1

saida = encontrar_esmeralda(caixas, esmeraldas, esmeralda_caos)

print(saida)
