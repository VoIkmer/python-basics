n=int(input())
plantacao=[]
H=0
R=0
a=0
b=0


for _ in range(n):  
    abobora=[int(p) for p in input().split()]
    plantacao.append(abobora)



x,y=input().split()
x=int(x)
y=int(y)

for j in range(x):
    a+=1

for i in range(y):
    b+=1

if a>b:
    for j in range(n):
        H+=plantacao[x][j]
    for i in range(n):
        R+=plantacao[i][y]
    R-=plantacao[x][y]

else:
    for j in range(n):
        H+=plantacao[x][j]
    for i in range(n):
        R+=plantacao[i][y]
    H-=plantacao[x][y]

print("Harry",H)
print("Ron",R)