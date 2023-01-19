from itertools import product

test_dict = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}

print("The original dictionary is : " + str(test_dict))

res = dict(zip(test_dict['month'], test_dict['name']))

print("Flattened dictionary : " + str(res))


def UncommonWords(A, B):

    count = {}

    for word in A.split():
        count[word] = count.get(word, 0) + 1

    for word in B.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]


A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

print(UncommonWords(A, B))

print("1) Fibonacci Sequence")


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))

print("2) Factorial of Number")


def factorial(n):
    if n == 1:
        return 1
    ans = n * factorial(n - 1)
    return ans


print(factorial(5))

print("3) Printing lists")

l = [1, 5, 10, 15, 20, 25, 30]

odd_elements = l[1::2]
print(odd_elements)

even_elements = l[0::2]
print(even_elements)

print("4) Find occurence of each element")

sample_list = [11, 25, 23, 35, 11, 25, 45, 60]

count_dict = dict()

for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("5) Bubble Sort")


def bubble_sort(arr):
    n = len(arr)
    for iter_num in range(n):
        for current in range(n - 1 - iter_num):
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
    i += 1

print("7) Sum of numbers")
sum = 0
# n = int(input("Enter num "))
n = 10

for i in range(1, n + 1, 1):
    sum += i
print(sum)

print("8) Number pattern")

row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print(" ")

print("Print pattern")

for num in range(10):
    for i in range(num):
        print(num, end=" ")
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
    arr[:] = arr[:i] + temp
    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))


def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = x


# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end=' ')


def dedupe_v1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y


def dedupe_v2(x):
    return list(set(x))


a = [1, 2, 3, 4, 3, 2, 1]
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
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))


def isMonotonic(A):

    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1))
            or all(A[i] >= A[i + 1] for i in range(len(A) - 1)))


A = [6, 5, 4, 4]

print(isMonotonic(A))


def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100

    print('The Simple Interest is', si)
    return si


simple_interest(8, 6, 8)


def compound_interest(principle, rate, time):

    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)


# Driver Code
compound_interest(10000, 10.25, 5)


def findArea(r):
    PI = 3.142
    return PI * (r * r)


# Driver method
print("Area is %.6f" % findArea(5))


def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list


# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)


def squaresum(n):
    sm = 0
    for i in range(1, n + 1):
        sm = sm + (i * i)

    return sm


n = 4

import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


def isFibonacci(n):

    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


for i in range(1, 11):
    if (isFibonacci(i) == True):
        print(i, "is a Fibonacci Number")
    else:
        print(i, "is a not Fibonacci Number ")

# Python 3 code to find sum
# of elements in given array


def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i

    return (sum)


arr = []
arr = [12, 3, 4, 15]

n = len(arr)

ans = _sum(arr)

print('Sum of the array is ', ans)


def largest(arr, n):

    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

#


def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = x


arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2

splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end=' ')

test_list = [1, 4, 5, 7, 8]

print("The list is : " + str(test_list))

counter = 0
for i in test_list:

    counter = counter + 1

print("Length of list using naive method is : " + str(counter))

lst = [1, 6, 3, 5, 3, 4]
i = 7
if i in lst:
    print("exist")
else:
    print("not exist")

total = 0

list1 = [11, 5, 17, 18, 23]

for ele in range(0, len(list1)):
    total = total + list1[ele]

print("Sum of all elements in given list: ", total)


def multiplyList(myList):

    result = 1
    for x in myList:
        result = result * x
    return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
     mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and \
     secondmax != list1[i]:
        secondmax = list1[i]

print("Second highest number is : ",\
 str(secondmax))


def Nmaxelements(list1, N):
    final_list = []

    for i in range(0, N):
        max1 = 0

        for j in range(len(list1)):
            if list1[j] > max1:
                max1 = list1[j]

        list1.remove(max1)
        final_list.append(max1)

    print(final_list)


list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

Nmaxelements(list1, N)

list1 = [10, 21, 4, 45, 66, 93]

for num in list1:

    if num % 2 == 0:
        print(num, end=" ")

list1 = [10, 21, 4, 45, 66, 93]

for num in list1:

    if num % 2 != 0:
        print(num, end=" ")

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):

    if num % 2 == 0:
        print(num, end=" ")

start, end = 4, 19

for num in range(start, end + 1):

    if num % 2 != 0:
        print(num, end=" ")

list1 = [11, -21, 0, 45, 66, -93]

for num in list1:

    if num >= 0:
        print(num, end=" ")

list1 = [11, -21, 0, 45, 66, -93]

for num in list1:

    if num < 0:
        print(num, end=" ")

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

for num in range(start, end + 1):

    if num >= 0:
        print(num, end=" ")

list1 = [11, 5, 17, 18, 23, 50]

for ele in list1:
    if ele % 2 == 0:
        list1.remove(ele)

print("New list after removing all even numbers: ", list1)

test_list = [5, 6, [], 3, [], [], 9]

print("The original list is : " + str(test_list))

res = [ele for ele in test_list if ele != []]

print("List after empty list removal : " + str(res))

test_list = [12, 67, 98, 34]

print("The original list is : " + str(test_list))

res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)

print("List Integer Summation : " + str(res))


def Repeat(x):
    _size = len(x)
    repeated = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated


list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
print(Repeat(list1))


def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length + 1)]
    return cu_list[1:]


lists = [10, 20, 30, 40, 50]
print(Cumulative(lists))

string = "geeks for geeks"
substring = "geeks"

s = string.split()

if substring in s:
    print("yes")
else:
    print("no")

string = "Sam quiz practice code"
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))

list1 = [1, 2, 3]

print("List1 before deleting is : " + str(list1))

list1 *= 0

print("List1 after clearing using *= 0: " + str(list1))

list1 = [1, 2, 3]
list2 = [5, 6, 7]

print("List1 before deleting is : " + str(list1))

del list1[:]
print("List1 after clearing using del : " + str(list1))

print("List2 before deleting is : " + str(list2))

del list2[:]
print("List2 after clearing using del : " + str(list2))

# Program to add two matrices using nested loop

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

A = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]

B = [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]

result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for i in range(len(A)):

    for j in range(len(B[0])):

        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)


def prod(val):
    res = 1
    for ele in val:
        res *= ele
    return res


test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

print("The original list : " + str(test_list))

res = prod([ele for sub in test_list for ele in sub])

print("The total element product in lists is : " + str(res))

n = "This is a python language"
s = n.split(" ")
for i in s:
    if len(i) % 2 == 0:
        print(i)


def check(string):

    string = string.lower()

    vowels = set("aeiou")

    s = set({})

    for char in string:

        if char in vowels:
            s.add(char)
        else:
            pass

    if len(s) == len(vowels):
        print("Accepted")
    else:
        print("Not Accepted")


if __name__ == "__main__":

    string = "SEEquoiaL"

    check(string)


def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    print("Without Order:", s)
    t = ""
    for i in str:
        if (i in t):
            pass
        else:
            t = t + i
        print("With Order:", t)


str = "HellomynameisHello"
removeDuplicate(str)

test_str = "GeeksforGeeks"

print("The original string is : " + test_str)

all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
else:
    all_freq[i] = 1
res = min(all_freq, key=all_freq.get)

print("The minimum of all characters in GeeksforGeeks is : " + str(res))

test_str = "GeeksforGeeks"

print("The original string is : " + test_str)

all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
else:
    all_freq[i] = 1
res = max(all_freq, key=all_freq.get)

print("The maximum of all characters in GeeksforGeeks is : " + str(res))

input_string = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"
input_string = input_string.replace(s1, s2)
print(input_string)

test_str = "geeksforgeeks"
s1 = "geeks"
s2 = "abcd"

s = test_str.split(s1)
new_str = ""

for i in s:
    if (i == ""):
        new_str += s2
    else:
        new_str += i

print(new_str)

test_dict = {
    'gfg': [5, 6, 7, 8],
    'is': [10, 11, 7, 5],
    'best': [6, 12, 10, 8],
    'for': [1, 2, 5]
}

print("The original dictionary is : " + str(test_dict))

res = list(sorted({ele for val in test_dict.values() for ele in val}))

print("The unique values list is : " + str(res))


def returnSum(myDict):

    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final


dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))


def Merge(dict1, dict2):
    return (dict2.update(dict1))


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print(Merge(dict1, dict2))

print(dict2)

import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), (2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")


def split_string(string):

    list_string = string.split(' ')

    return list_string


def join_string(list_string):

    string = '-'.join(list_string)

    return string


if __name__ == '__main__':
    string = 'Geeks for Geeks'

    list_string = split_string(string)
    print(list_string)

    new_string = join_string(list_string)
    print(new_string)

s = 'Geeks for Geeks'
print(s.split(" "))
print("-".join(s.split()))

test_str = 'Gfg is best . Gfg also has Classes now. \
				Classes help understand better . '

print("The original string is : " + str(test_str))

repl_dict = {'Gfg': 'It', 'Classes': 'They'}

test_list = test_str.split(' ')
res = set()
for idx, ele in enumerate(test_list):
    if ele in repl_dict:
        if ele in res:
            test_list[idx] = repl_dict[ele]
        else:
            res.add(ele)
res = ' '.join(test_list)

print("The string after replacing : " + str(res))

test_str = 'It is the best thing ever for CS'

print("The original string is : " + str(test_str))

word_list = ["best", 'CS', 'for']

repl_wrd = 'gfg'

res = ' '.join(
    [repl_wrd if idx in word_list else idx for idx in test_str.split()])

print("String after multiple replace : " + str(res))

test_tup = (5, 20, 3, 7, 6, 8)

print("The original tuple is : " + str(test_tup))

K = 2

res = []
test_tup = list(sorted(test_tup))

for idx, val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)

print("The extracted values : " + str(res))

test_tuple1 = (4, 5)
test_tuple2 = (7, 8)

print("The original tuple 1 : " + str(test_tuple1))
print("The original tuple 2 : " + str(test_tuple2))

res = [(a, b) for a in test_tuple1 for b in test_tuple2]
res = res + [(a, b) for a in test_tuple2 for b in test_tuple1]

print("The filtered tuple : " + str(res))

test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

print("The dictionary before performing remove is : " + str(test_dict))

removed_value = test_dict.pop('Mani')

print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))

print('\r')

removed_value = test_dict.pop('Manjeet', 'No Key found')

print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))


def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))

test_dict = {'gfg': [7, 6, 3], 'is': [2, 10, 3], 'best': [19, 4]}

print("The original dictionary is : " + str(test_dict))

res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])

print("The sorted dictionary : " + str(res))


def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr


arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))


def search(arr, x):

    for i in range(len(arr)):

        if arr[i] == x:
            return i

    return -1


def selectionSort(array, size):

    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)


def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

from datetime import datetime

now_method = datetime.now()

currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)


def largest(arr, n):
	max = arr[0]
	for i in range(1, n):
		if arr[i] > max:
			max = arr[i]
	return max


arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr, n)
print("Largest in given array ", Ans)

def multiplyList(myList):

	result = 1
	for x in myList:
		result = result * x
	return result

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
print()

a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))
print()

x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)
