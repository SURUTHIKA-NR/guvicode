h1,h2=list(map(int,input().split()))
cunt=0
for h in range(h1+1,h2):
    if h>1:
        for i in range(2,h):
            if h%i==0:
                break
        else:
            print(h,end=" ")
