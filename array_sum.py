arraysize=int(input())
sumsize=int(input())
arraylist=list(map(int,input().split()))
sumarray=0
for i in range(0,sumsize):
  sumarray=sumarray+arraylist[i]
print(sumarray)
