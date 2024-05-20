n=int(input())
d=0

while n!=0:
    L=[]
    for _ in range(n):
        j,z=input().split()
        j=int(j)
        z=int(z)
        h=j-z
        d+=1
    print("Teste" + " " + str(d))
    print(h)
    print(" ")
    n=int(input())