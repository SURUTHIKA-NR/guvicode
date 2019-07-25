ab,cd=input().split()
li=list(map(int,input().split()))
li.sort(reverse=True)
print(li[cd-1])
