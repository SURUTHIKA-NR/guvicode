leapyr=int(input())
if (leapyr%4==0 and leapyr%100!=0) or leapyr%400==0:
  print("Yes")
else:
  print("No")
