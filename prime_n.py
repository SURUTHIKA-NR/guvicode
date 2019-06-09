prm=int(input())
cut=0
for f in range(1,prm+1):
    if prm%f==0:
        cut=cut+1 
if cut==2:
    print("yes")
else:
    print("no")

