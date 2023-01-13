n= int(input("marks: "))
if n>90:
  print("excellent")
elif n>80 and n<90:
  print("pretty good")
elif n>70 and n<80:
  print("fair")
elif n>60 and n<70:
  print("meets expectations")
elif n<60 or n==60:
  print("below par")