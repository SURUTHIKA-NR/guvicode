n,a,d=input().split()
to=0
va=int(a)
for i in range(int(n)):
    to=to+va
    va=va+int(d)
print(to)
