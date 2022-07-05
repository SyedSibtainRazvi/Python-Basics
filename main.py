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
  
def select_sort(arr):
  n = len(arr)
  for iter_num in range(n):
    min_index = iter_num
    for current in range(iter_num + 1, n):
      if arr[current] < arr[min_index]:
        min_index = current
        arr[min_index], arr[iter_num] = arr[iter_num], arr[min_index]

select_sort(arr)
print(arr)

print("6) Natural numbers")
i = 1
while i <= 10:
  print(i)
  i +=1

print("7) Sum of numbers")
sum = 0
# n = int(input("Enter num "))
n = 10

for i in range(1, n + 1, 1):
  sum +=i
print(sum)

print("8) Number pattern")

row = 5
for i in range(1, row + 1, 1):
  for j in range(1, i + 1):
    print(j, end = ' ')
  print(" ")


print("Print pattern")

for num in range(10):
    for i in range(num):
        print (num, end=" ")
    print("\n")

print("Asterick pattern")

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")