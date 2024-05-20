N = int(input())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
D = list(map(int, input().split()))

a=0

for i in range(N):
        if u[i] + v[i] != D[i]:
                a+=1
        else:
                a=0

if a!=0:
        print("NOPE :(")
else:
        print("OK")
