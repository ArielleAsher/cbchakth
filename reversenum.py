n=int(input("n: "))

n=str(n)
lst=[]
for i in n:
  lst.append(i)
  
L=len(lst)
for i in range(L,0,-1):
  print(lst[i-1])