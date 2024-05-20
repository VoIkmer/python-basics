n = int(input())
a=n*2-1
b=1
for j in range(1,n+1):
    x=a-b
    print(" "*((x)//2),str(j)*b," "*((x)//2),sep="")
    b+=2
    