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