def sum(n):
  if(n==0):
    return 0
  Totalsum = n+(sum(n-1))
  return Totalsum
print(sum(6))