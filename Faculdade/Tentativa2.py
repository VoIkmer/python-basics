e,p=input().split()
e=int(e)
p=int(p)
a=0
while True:
    e-=p
    p-=1
    a+=1

    if e<=0 or p<=0:
        break
if e>0:
    print("F")
else:
    print(a)