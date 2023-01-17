#hcf

n1= int(input("n1: "))
n2= int(input("n2: "))

hcf=1

if n1<n2:
  chotan=n1
else:
  chotan=n2
  
for i in range(1,chotan+1):
  if n1%i==0 and n2%i==0:
    hcf=i
  else:
    pass

#LCM
n=n1*n2
lcm=(n)/hcf
print("LCM is" ,lcm)

#GCD
print("GCD is: ",(n/lcm))