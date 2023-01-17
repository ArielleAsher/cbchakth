n=int(input("enter num: "))

l=[]
def prime(n):
  flag=0
  for j in range(2, n//2 + 1):
    if n %j==0:
      flag=1
  return flag
for i in range(1, n+1):
  if prime(i)==0:
    l.append(i)

for i in l:
  if n%i==0:
    print(i)