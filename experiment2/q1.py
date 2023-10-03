def sumOfDivisor(n):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
        
    return sum


Number1 = int(input("Enter 1st Number : "))
Number2 = int(input("Enter 2nd Number : "))


if(Number1 == sumOfDivisor(Number2) and Number2 == sumOfDivisor(Number1)):
    print("yes")
else:
    print("no")
