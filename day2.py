# Condition Statements
# if statement:
if (3>2):
    print("3 is greater then 2!!")

# Multiple of 5:
number = int(input("Enter any number to check, number is divisible by 5 or not: "))
if(number % 5 == 0):
    print(number , " is divisible by 5")
else:
    print(number , " is not divisible by 5")


# Odd or Even
checkNum = int(input("Enter Number to check wheter the number is prime or not: "))
if(checkNum % 2 == 0):
    print(checkNum , " is Even")
else:
    print(checkNum," is odd")

# Nested if and Multi-way ,if else-if Statement:
Marks = int(input("Enter your marks: "))

if(Marks >= 90):
    grade = 'A'
elif(Marks >=80):
    grade = 'B'
elif(Marks >= 70):
    garde = 'C'
elif(Marks >= 60):
    grade = 'D'
else:
    grade = 'F'


print("You Score : ",grade)

# While loop
count = 0

while count <=10:
    print(count , "Happy")
    count = count + 1

# Table using While
TableOF = int(input("Enter Number : "))
cout = 1
while cout <=10:
    print(TableOF," * ",cout," = ",TableOF * cout)
    cout = cout + 1

n = int(input("Enter Number to get sum till 1 : "))
sum = 0
while n >=1:
    sum = sum + n
    n = n -1

print("Sum from 1 to ", n , " is ", sum)


FirstNum = int(input("Enter First number : "))
SecondNum = int(input("Enter Second number : "))
SumOF = 0

if(FirstNum>SecondNum):
    Min = SecondNum
    Max = FirstNum
else:
    Min = FirstNum
    Max = SecondNum

while(Min <= Max):
    SumOF = SumOF + Min
    Min = Min + 1

print("Sum of All numbers between ", FirstNum ," and " , SecondNum ," = ", SumOF)