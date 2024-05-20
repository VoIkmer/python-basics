import math      

Xm,Ym,Xr,Yr=input().split()
Xm=int(Xm)
Ym=int(Ym)
Xr=int(Xr)
Yr=int(Yr)

d=math.sqrt((Xm-Xr)**2) + math.sqrt((Ym-Yr)**2)
d=int(d)
print(d)
