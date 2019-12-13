"""
# Here is some of the code for the final. I will show you how to install python at home so you can practice.

# my advice is to practice and make sense of easiest problems first

# Problem 1 - create variables with 6 different data types
# call print and type functions to show the daya types
age = 16
print(type(age))
value = 2.64
print(type(value))
name = 'Fred'
print(type(name))
answer = True
print(type(answer))
names = ['Fred','George']
print(type(names))
names = ('Fred', 'George')
print(type(names))
names = {'Fred','George','Fred'}
print(type(names))
#--------------------------------------------------------------
#Problem 2 convert base2 to base10 on paper - we will continue to practice this during each class
#--------------------------------------------------------------
#Problem 3 convert base10 to base2 on paper - we will continue to practice this during each class
#--------------------------------------------------------------
#Problem 4 convert base2 to base10 with code
base2Str = '10110110'
base2Int = int(base2Str)
base10 = 0

for i in range(len(base2Str)):
    digit = base2Int % 10
    base10 = base10 + digit* 2**i
    base2Int = base2Int//10

print(base10)
#--------------------------------------------------------------
#Problem 5 convert base10 to base2 with code
base10 = 237
base2 = ''

while base10 > 0:
    digit = base10 % 2
    base2 = str(digit) + base2
    base10 = base10//2

print(base2)
#--------------------------------------------------------------
#Problem 6 add numbers in a list with for loop (i in range)
numbers = [2,5,8,3,7]
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]

print(total)
#--------------------------------------------------------------    
#Problem 7 add numbers in a list with for loop (for each)
numbers = [2,5,8,3,7]
total = 0
for num in numbers:
    total = total + num

print(total)
#--------------------------------------------------------------
#Problem 8 create acronym from list of strings
names = ["Huron","Ontario","Michigan","Erie","Superior"]
acronym = ''
for word in names:
    acronym = acronym + word[0:1]
print(acronym)
#--------------------------------------------------------------
#Problem 9 - find biggest or smallest number in a list
numbers = [2,5,8,3,7]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print(biggest)
#--------------------------------------------------------------
#Problem 10 - add odd numbers in a list
numbers = [2,5,8,3,7]
total = 0
for i in range(len(numbers)):
    if numbers[i]%2 == 1:
        total = total + numbers[i]
print(total)
#--------------------------------------------------------------
#Problem 11 - add numbers in list that are not multiples of 5 (this value can vary)
numbers = [2,5,8,3,7]
total = 0
for num in numbers:
    if num%5 != 0:
        total = total + num
print(total)
  """

# Python List
hello = [1,2,3,4,5]
total = 0
for num in hello:
    total += num
print(total)
   

names = ["Huron","Ontario","Michigan","Erie","Superior"]
acronym = ''
for word in names:
    acronym = acronym + word[0:1]
print(acronym)


   




 
