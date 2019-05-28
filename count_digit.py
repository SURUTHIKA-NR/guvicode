digit=int(input())
digits=digit
digcnt=0
while digits>0:
  digrem=digits%10
  digcnt=digcnt+1
  digits=digits//10
print(digcnt)
