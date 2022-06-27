print("1) Fibonacci Sequence");

def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))


print("2) Factorial of Number")

def factorial(n):
  if n == 1:
    return 1
  ans = n * factorial(n-1)
  return ans


print(factorial(5))