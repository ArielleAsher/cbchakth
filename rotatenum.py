w=int(input("number: "))
k=int(input("no. of rotations"))
w=str(w)
if k>0 or k==0:
  L=len(w)-k
  str1=w[0:L]
  str2=w[L:L+k+1] 
  s=str2+str1
  print (s)

else:
  k=abs(k)
  str1=w[0: k]
  str2=w[k:len(w)]
  s=str2+str1
  print(s)