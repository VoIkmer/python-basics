n=int(input())
lista = [int(t) for t in input().split()]

tempo=sorted(lista)[:8]

print (' '.join(map(str, tempo)))