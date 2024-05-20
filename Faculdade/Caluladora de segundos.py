n = int(input())
h = int(n//3600)
m = int((n%3600)//60)
s = int(n%60)

print(str(h)+"h",str(m)+"m",str(s)+"s")