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