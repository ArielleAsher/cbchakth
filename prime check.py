def prime(f):
    flag=0
    for j in range(2,(i//2+1)):
      if i%j==0:
        flag=1       
    return(flag) 
t=int(input("how many numbers?: "))
lst=[]
for i in range(0,t):
  n=int(input("number"))
  lst.append(n)
for i in lst:
  if prime(i)==1:
    print('not prime')
  else:
    print('prime')

  
  
    
      
    
      
      
    
    