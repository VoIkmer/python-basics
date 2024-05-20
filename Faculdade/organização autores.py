n = int(input())
autores = []

def abreviar(a):
    particao = a.split()
    nomes_abreviados = [nome[0].upper() + "." for nome in particao[:-1]]
    ultimo_sobrenome = particao[-1].capitalize()  # Corrigido para deixar a primeira letra do sobrenome em maiúscula
    return " ".join(nomes_abreviados) + " " + ultimo_sobrenome

for _ in range(n):
    a = input().lower()
    a_abreviacao = abreviar(a)
    autores.append(a_abreviacao)
    
print("\n".join(autores))
