# 1. PRINT
print("Hello World")


# 2. VARIABLES
name = "Jateen"      # string
age = 20             # int
price = 99.5         # float
student = True       # bool


# 3. INPUT
name = input("Name: ")
age = int(input("Age: "))


# 4. OPERATORS
# +    # add
# -    # subtract
# *    # multiply
# /    # divide
# %    # remainder
# **   # power
# //   # floor division


# 5. IF / ELSE
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")


# 6. FOR LOOP
for i in range(5):
    print(i)
# Output: 0 1 2 3 4


# 7. WHILE LOOP
i = 1
while i <= 5:
    print(i)
    i += 1


# 8. LIST
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])     # Apple
fruits.append("Orange")
fruits.remove("Banana")


# 9. FUNCTION
def add(a, b):
    return a + b

print(add(5, 3))


# 10. PRIME NUMBER
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 11. STRING
name = "Python"

print(len(name))      # length
print(name.upper())   # PYTHON
print(name.lower())   # python


# 12. DICTIONARY
person = {
    "name": "Jateen",
    "age": 20
}

print(person["name"])


# 13. COMMENTS
# This is a comment


# 14. COMPARISON
# ==    # equal
# !=    # not equal
# >     # greater
# <     # smaller
# >=    # greater/equal
# <=    # smaller/equal


# 15. LOGICAL
# and
# or
# not


# ----------------------------questions------------------------ #

#
number1 = input ()
number2 = input ()
sum = number1+number2
print(sum)

#
number1 = int(input()) 
number2 = int(input())
sum = number1 + number2
print(sum)

#
pens = 12*5
notebooks = 45*3
erasers = 8*2
total = pens + notebooks + erasers - 20
print("final Amount:",total)

#
salary = 50000
salary += salary * 10 / 100
salary -= salary * 5 / 100
print("Final Salary:", salary)

#
marks = 78
passing_marks = 40
passed = marks >= passing_marks
print("Passed:", passed)

#
a = 10
b = 5
print("a & b:", a & b)

# 7 september
 
time = int(input("enter the no of hour you have" ))
if time >= 6 :
    print("go for sunset")
else:
    print("go for bowling")

#
budget = int(input("enter the amount you have"))
if budget>2000: 
   print("go for sunset")

elif budget>1000:
   print ("go to park")
         
elif budget >500:
   print("go to coffee")
else:
   print("sit at home an have tea.")

#
num = int(input("enter your number"))
if num > 0:
   print("positive")
if num < 0:
  print("negative")
if num == 0: 
  print("zero")

#
username = input("enter the username:")
passward = input("enter the passward:")

if username == "admin" and passward == "python123":
    print("login ")

else :
   print("invalid login")

#
number = int(input("enter the number"))
if number % 3 and 5 == 0:
    print("divisible by both 3 and 5 ")
elif number % 3==0: 
    print(("divisible by 3"))
elif number % 5==0 :
    print("divisible by 5") 

#
marks  = int(input("enter marks"))
attendance = int(input("enter attendance"))
if marks < 40:
    print("fail")
elif marks >= 40 and attendance < 75:
    print("fail due to attendance")
elif marks >= 90 and attendance >= 90:
    print("outstading")
elif marks >= 75 and attendance >= 80 :
    print(" excellant")
elif marks >= 60 and attendance >= 75:
    print("good")
else:
    print("pass")  


# 8- sep.-2026

budget = int(input("enter the amount you have"))
time = int(input("enter the time you have"))
if budget >= 2000 and time >= 6:
    print("hills")
if time >3 and time<6:
    print("rest.")
elif time <= 3 :
    print(" netflix and chill")

if budget > 1000 and budget < 2000 and time >8:
    print("benglore visit")
else:
    print("no plan")        

#
for count in range(1,6):
    friend=input("write the name")
    print(friend)                  

#
#find even numbers in this range

for count in range(1,50):
 if count % 2==0:
    print(count)

# for sum of n numbers
n = int(input("number:"))
sum = 0
for counter in range (1,n+1):
  sum = sum + counter
print(sum)

# for sum of even number in n numbers
n = int(input("number:"))
sum = 0
for counter in range (1,n+1):
 if counter%2==0:
   sum = sum + counter
print(sum)

# for counting
n = 10
count =1

while count <= n:
    print(count)
    count= count +1

# find sum of digits
# 153 = 1+5+3 = 9
# 153%10 = 3
# 153//10 = 15
# repeat on 15
# 15%10 = 5
# 15//10 = 1
# then sum of 3+5+1

n = int(input("enter the number:"))
sum = 0
while n>0:
   remainder = n%10
   n=n//10
   sum = sum + remainder
print(sum)


# for check positive ,negetive ,zero
n = int(input("Enter a number: "))  
if n > 0:
  print("positive")
  if n%2==0:
    print("even")
  else:
    print("odd")
elif n < 0:
   print("negetive")
   if n%2==0:
     print("even")
   else: 
    print("odd")  
else:
  print("zero")

# 9 sep. 2026

# for row and column
column = int(input())
row = int(input())
for i in range(1,column+1):
    for i in range(1,row+1):
        print("*",end=" ")
    print()  

#
r = int(input())
c = int(input())
for rows in range(1,r+1):
    for columns in range(1,c+1):
        if rows == 1 or rows== 5 or columns == 1 or columns == 4 :
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()

#
n = int(input())

for r in range(1,n+1):
    for c in range(1,r+1):
        print("*",end=" ")
    print()

#
n = int(input())
for rows in range(n,0,-1):
    for columns in range(rows):
        print("*",end = " ")
    print()

#
i = 1
while i <= 5:
    print(i)
    i += 1

# for password
# not equal because jab tak correct password nahi tab tak loop chalega
password = "   "
while password != "Jateen" :
    password = input("enter pass :")
print("access granted")

#
count  = 1 
while count <= 60:
    print("RAM RAM")
    count += 1
print("loop finished , count =" , count)

# nested loops
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print( )

# 10-sep.-2026

# Using print
def add_print(a, b):
  print("Sum is:", a + b)
add_print(5, 10)
# Using return
def add_return(a, b):
  return a + b
result = add_return(5, 10)
print("Sum is:", result)

#
def square_print(num):
    print("square is:",num*num)
square_print(5) 
square_print(9) 

# Define the function

def function(a, b):
 area = a * b
 perimeter = 2 * (a + b)
 return area, perimeter
# Take input from user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
# Call the function and get results
area, perimeter = function(a, b)
# Print nicely
print("Area is:", area)
print("Perimeter is:", perimeter)

# when use print
def rectangle_print(length, width):
 area = length * width
 perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)
rectangle_print(10, 5)   


# 11-sep.-2026

def add(var1,var2=10):
 return  var1 + var2

sum= add(2,20)
print(sum)

#
def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
n = int(input("Enter a number: "))

if check_prime(n):
    print("Prime number")
else:
    print("Not a prime number")


#

def armstrong(n):
    original_n=n
    sum= 0
    while(n>0):
        remainder = n%10
        sum+=remainder**3
        n=n//10

    if sum==original_n:
        return True
    else:
        return False
    print ("")

#Q1
def calculator(a,b,operator):
 if operator == "+":
    return a+b
 elif operator == "-":
        return a-b
 print(calculator(a,b,operator))

# 14-sep.-2026
celebrationlist = ["ladoo", "modak", "statue","musak"]
celList = [1000,1000,1,20]

print(celebrationlist[0])
print(type(celebrationlist[0]))
print(type(celList[0]))

#
celebrationlist = ["ladoo", "modak", "statue","musak"]
celList = [1000,1000,1,20]
for items in celebrationlist:
    print(items)

# create a list of integers
# output the sum of all the items

list_integers = [10,20,30,44,55]
sum = 0

for number in list_integers:
    sum = sum + number
print(sum)

# create a list of integers
# print it in reverse but only the even index 
# try to incorporate the length method as well (len())


numbers = [10,20,30,40,50,60,70,80,90]
for iterator in range(-2,-11,-2):
  print(numbers[iterator] ,end=" ")

#
numbers = [11,22,33,44,55,66,77,88,99,111]

for items in range(0,len(numbers)):
    print(numbers[items])

for num in numbers:
    print(num)

#
celebration_things = ["modak","ladoo","musak"]
print(celebration_things)

celebration_things.append("aarthi")
print(celebration_things)

celebration_things.append(["flowers","statue"])
print(celebration_things)

for items in celebration_things:
    print(items)
    print(type(items))

#
celebration_things = ["modak","ladoo","musak"]
print(celebration_things)

celebration_things.append("aarthi")
print(celebration_things)

celebration_things.insert(3,"sunflower")
print(celebration_things)
celebration_things.insert(11,"sunflower")
print(celebration_things)

#
list = [11,22,33,44,55,66,77,88]
even_count = 0
odd_count = 0
for num in list:
    if num%2 ==0:
        even_count += 1
    else:
        odd_count += 1
print(list)
list.insert(0,odd_count)
list.append(even_count)
print(list)

#
numbers = [25,10,45,5,30]

largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num> largest:
        largest = num

    if num < smallest:
        smallest = num
print("largest:",largest)
print("smallest:",smallest)

# 15-sep.-2026

list1 = [10,20,30,40,50]

var = list1[len(list1)-1]
list1.remove(50)
list1.insert(0,var)

print(list1)

# pop
list1 = [10,20,30,40,50]
list1.pop(3)
print(list1)
list1.pop( )
print(list1)

# list[start : stop : step]
list1 = [10,20,39,45,12]
print(list1)

print(list1[1:4:1])

#
list1 = [10,20,39,45,12]
print(list1)

print(list1[4:1:-1])

#
list1 = [10,20,39,45,12]
print(list1)

print(list1[:])

# for revarce
list1 = [10,20,39,45,12]
print(list1)

print(list1[: :-1])

# for signwise distribution
list = [1,3,-4,6,-7,2,-44,33,-77]

listP = []
listN = []
for iterator in list :
    if iterator >0:
        listP.append(iterator)
    elif iterator<0:
        listN.append(iterator)
print(listP)
print(listN)

#
# take a list which contains the number 2 in multiple
# indexes
# Return a list which contains all the index of 2

list = [2,4,6,8,10,12,14,16]
list_index = []

for i in range(0,len(list_index)):
    if list[i] == 2:
        list_index.append(i)
print(list_index)

# for remove one number
list = [2,4,6,8,10,12,14,16]
del list[4]
print(list)

#
list = [2,4,6,8,10,12,14,16]
del list[1:6:1]
print(list)

# sort
numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)

# for sort reverse
numbers = [5,2,8,1,3]
numbers.sort(reverse=True)
print(numbers)

# sorted
list = [5, 2, 8, 1, 3]
print(sorted(list))


#mix questions
numbers = [40,10,70,20,90,30,60]
print(numbers[::-1])
numbers[2]=75
print(numbers)
numbers.append(100)
print(numbers)
del numbers[3]
print(numbers)
numbers.sort()
print(numbers)

#
marks = [78,45,92,67,55,88,34,95]

print(marks[0],marks[-1]) # Question is print first and last marks
print(marks[2:7:1])
marks[6]=64
print(marks)
marks.append(100)
print(marks)
marks.pop(3)
print(marks)
marks.sort(reverse=True)
print(marks)
marks.sort()
print(marks)
print(marks[0:3:1])
print(marks)

#
marks = [25,80,15,60,45,90,30,70]
print(marks[::-1])
print(marks[1],marks[3],marks[5],marks[7])
marks[2]=100
marks[6]=50
print(marks)
marks.append(120)
print(marks)
marks.pop(4)
print(marks)
marks.sort()
print(marks)
print(marks[0:4:1])
print(marks)

#------------tuples--------------------------------------------------------------------------------------------------------#
# we are not remove anythink from tuples#

t = (10, 20, 30, 40, 50)
print(t[0]) # 10
print(t[-1]) # 50
print(t[1:4]) # (20, 30, 40)
print(t[:3]) # (10, 20, 30)

#Tuple Operations
#(a) Concatenation
t1 = (1, 2)
t2 = (3, 4)
t3 = (t1+t2)
print(t3) # (1, 2, 3, 4)
#(b) Repetition
t = ("Hi", 2)
print(t * 3) # ("Hi", 2, "Hi", 2, "Hi", 2)

#
t = (10, 20, 30)
print(20 in t) # True
print(50 not in t) # True

#
t = (5, 1, 9, 3, 9)
print(len(t)) # 5
print(min(t)) # 1
print(max(t)) # 9
print(sum(t)) # 27

#

l1 = (10,22,33,10,-11,-10,10,9,-45,10)
l2 = list()
for i in l1:
    if not i in l2:
        print(l1.count,i)
        l2.append(i)

# your are given a binary sequence number in form of the tuple write 
# the tuple (1,0,1,1,1,0,0,1,1,1,1,0) find out largest sequence containing posibile
tup1= (1,0,1,1,1,0,0,1,1,1,1,0)

curr=0
max_s=0
for element in tup1:
    if element==1:
        curr+=1
        if curr>max_s:
            max_s=curr
    else:
        curr=0
print(max_s)

# for find a index
tup1= (1,0,1,1,1,-22,0,1,1,1,1,0)
print(tup1.index(-22))

#
tup1= (1,0,1,1,1,-22,0,1111,1,1,1,0)
print(max(tup1))
print(min(tup1))
print(sum(tup1))
print(sorted(tup1))
print(type(tup1))
print(-20 in tup1)

# find the intersection of 2 tuples
# without using sets:
# t1 = (1,2,3,4,5,6)
# t2 = (4,5,6,7,8,9)

t1 = (1,2,3,4,5,6)
t2 = (4,5,6,7,8,9)

intersection = tuple(no for no in t1 if no in t2)
print(intersection)

# method 2
result = ()
for num in t1:
    if num in t2:
        result = result + (num,)
print(result)

#
t1 = (1,2,3,4,5,6,7)
a,b,*c = t1
print("A:",a)
print("B:",b)
print("C:",c)

#
t1 = (1,2,3,4,5,6,7)
a,*b,c = t1
print("A:",a)
print("B:",b)
print("C:",c)

#numbers = (10,20,30,40,50,60,70)
a,b,c,d,*e = numbers
print(*e,a,b,c,d)

result = numbers[-3:]+numbers[:4]
print(result)

#
# find second largest number
numbers = (45,12,78,34,78,90,23,90,56)
largest = 0
second = 0
for n in numbers:
    if n > largest:
        second=largest
        largest=n
    elif n > second :
        second = n
print(second)

# find student with the highest total marks 
# 1 total marks 
# 2 avreage marks
data = (
    ('Alice', 78,85,91),
    ('Bob', 88,76,95),
    ('Charlie',92,89,84),
    ('David',75,90,87)
)
higest_marks = 0
for i in data:
    total = i[1]+i[2]+i[3]
    if total>higest_marks:
        higest_marks=total
        name=i[0]
print(higest_marks)
print(name)

#
tup1 = ([10,20],[-22,44,-11])
a,b=tup1
a.append(90)
print(tup1)

# remove multiple tuples

data = [(10,20),(30,40,),(10,20),(50,60),(30,40),(70,80),(10,20)]
unique_list = []
for element in data:
    if element not in unique_list:
        unique_list.append(element)
print(unique_list)