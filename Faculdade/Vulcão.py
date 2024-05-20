t=int(input())
p=int(input())
a=0
a=int(a)
while p>0:
    p=int(input())
    if p>a:
        a=p
if a>t:
    print("ALARME")
else:
    print("O Havai pode dormir tranquilo")
