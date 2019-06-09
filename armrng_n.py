arms1,arms2=list(map(int,input().split()))
for arms in range(arms1,arms2):
    armss=arms
    ar=armss
    arm=0
    le=len(str(arms))
    while(ar>0):
        re=ar%10
        arm=arm+re**le
        ar=ar//10
    if armss == arm:
        print(arm,end=" ")
