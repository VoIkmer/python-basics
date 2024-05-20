p,r=input().split()
p=int(p)
r=int(r)

if bool(p)==False:
    print("C")
elif bool(p)==True and bool(r)== False:
    print("B")
else:
    print("A")
