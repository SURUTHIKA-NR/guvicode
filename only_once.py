a=int(input())
li=list(map(int,input().split()))
for k in li:
   if li.count(k)==1:
      print(k)
