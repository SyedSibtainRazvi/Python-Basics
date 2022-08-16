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

print("Add list to set")

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)
print(sample_set)

print("Identical numbers in two sets")

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

print("Update set if element does not exist")

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)

print("Print list in reverse")
list1 = [10, 20, 30, 40, 50]

size = len(list1) - 1
for i in range(size, -1, -1):
    print(list1[i])


print("New Pattern")

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
 

arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))
 
def splitArr(arr, n, k): 
    for i in range(0, k): 
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j + 1]
          
        arr[n-1] = x
          
  
# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
  
splitArr(arr, n, position)
  
for i in range(0, n): 
    print(arr[i], end = ' ')

def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print(dedupe_v1(a))
print(dedupe_v2(a))

def swapList(newList):
    size = len(newList)
     
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))


def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
A = [6, 5, 4, 4]
  
print(isMonotonic(A))

def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
     
simple_interest(8, 6, 8)