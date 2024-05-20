frase = input()
q, p = input().split()
q = int(q)

def contar_ocorrencias(frase, p):
    frase_sem_espaco = ""
    for letra in frase:
        if letra != " ":
            frase_sem_espaco += letra.lower()
    tamanho_p = len(p)
    tamanho_frase = len(frase_sem_espaco)
    ocorrencias = 0
    i = 0
    while i < tamanho_frase:
        if frase_sem_espaco[i:i+tamanho_p] == p:
            ocorrencias += 1
            i += tamanho_p
        else:
            i += 1 
    return ocorrencias

ocorrencias = contar_ocorrencias(frase, p)
if ocorrencias == q:
    print(ocorrencias)
    print("SIM!")
else:
    print(ocorrencias)
    print("NAO!")
