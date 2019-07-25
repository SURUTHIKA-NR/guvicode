ab=int(input())
l2=list(map(int,input().split()))
l4=[]
for i in l2:
    if l2.count(i)>1:
        if i not in l4:
            l4.append(i)
if len(l4)==0:
    print("unique")
else:

    l4.sort()
    print(*l4,end=' ')
