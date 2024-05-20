r=int(input())
A=0
B=0
while r!=0:
    for i in range(r):
        a,b=input().split()
        a=int(a)
        b=int(b)
        A+=a
        B+=b
        if A>B:
            c="Aldo"
        elif B>A:
            c="Beto"
    print("Teste" + " " +str(i))
    print(c)
    r=int(input())

