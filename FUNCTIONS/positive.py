list=[34,-65,23,-9,-26,4,17]

def numbers(num):
  pos= 0
  neg=0
  for j in num:
      if(j>0):
        pos=pos+1
      else:
        neg=neg+1
  print("Number of positive numbers:",pos)
  print("Number of negative number:",neg)
numbers(list)
