pal=int(input())
pali=pal
rvs=0
while(pali>0):
    rdr=pali%10
    rvs=rvs*10+rdr
    pali=pali//10
if rvs==pal:
    print("yes")
else:
    print("no")
