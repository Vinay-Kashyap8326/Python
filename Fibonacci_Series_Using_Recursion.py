def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
n = int(input("Enter Number: "))
print("\nFibonacci series:",end=" ")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")