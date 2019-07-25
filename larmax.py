a=int(input())
s=[]
l1=list(map(int,input().split()))
if sum(l1)>0:
    l1.sort(reverse=True)
    for j in l1:
        print(j,end='')
else:
    print(0)
