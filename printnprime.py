def prime(n):
  flag=0
  for j in range(2, n//2 + 1):
    if n %j==0:
      flag=1
  return flag
  
low=int(input("low: "))
high= int(input("high: "))

for i in range(low, high+1):
  if prime(i)==0:
    print(i)