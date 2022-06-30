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


print("3) Printing lists")

l = [1,5,10,15,20,25,30]

odd_elements = l[1::2]
print(odd_elements)

even_elements = l[0::2]
print(even_elements)


print("4) Find occurence of each element")

sample_list = [11 , 25 , 23 , 35 , 11 , 25, 45 , 60]

count_dict = dict()

for item in sample_list:
  if item in count_dict:
    count_dict[item] += 1
  else:
    count_dict[item] = 1

print(count_dict)

arr = [9,8,7,6,5,4,3,2,1]
print("5) Bubble Sort")

def bubble_sort(arr):
  n = len(arr)
  for iter_num in range(n):
    for current in range(n-1-iter_num):
      if arr[current] > arr[current + 1]:
        arr[current], arr[current + 1] = arr[current + 1], arr[current]

bubble_sort(arr)
print(arr)
  
