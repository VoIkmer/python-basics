n=input()
p,c,q=input().split()
p=int(p)
c=str(c)
q=int(q)    
n=int(n)

if c== "+":
    r=p+q
elif c== "*":
    r=p*q
r=int(r)
if r >= n:
    print("OVERFLOW")
else:
    print("OK")