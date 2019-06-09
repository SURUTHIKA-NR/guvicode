arms=(input())
armss=int(arms)
ar=armss
arm=0
le=len(arms)
while(ar>0):
    re=ar%10
    arm=arm+re**le
    ar=ar//10
if armss == arm:
   print("yes")
else:
   print("no")
