
N=int(input())
x=1
j=0
z=0
while N!=0:
    LI=[]
    for i in range(N):
        J,Z=(input().split())
        J,Z=int(J),int(Z)
        j+=J
        z+=Z
        LI.append(j-z)
        if i==(N-1):
            print("Teste",x)
            for d in LI:
                print(d)
                d+=1
            x+=1
    N=int(input())