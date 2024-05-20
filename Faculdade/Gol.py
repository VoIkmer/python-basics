# z é a direção do zagueiro 
# g é a direcão que o goleiro pega
# d é a direção que o atacante vai
# c é onde o atacante chuta
z,g = input().split()
d,c = input().split()

if d==z:
    print("Driblado")
    if c != g:
        print("... e o goleiro pega")
    elif c == g:
        print("Gol")
else:
    print("Bloqueado")