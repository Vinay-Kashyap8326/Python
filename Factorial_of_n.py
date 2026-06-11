def factorial(n):
  if(n==0):
    return 1
  Fact = n * factorial(n-1)
  return Fact
print("Factorial is:",factorial(5))