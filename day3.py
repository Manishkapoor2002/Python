import math
# for,for-else Loops:
# for i in range(1,11,1): #it will print from 1 to 10(n-1):
#     print("hello World!!",i)

# for i in range(2,22,2):
#     print(i)

# for i in range(5):
#     print(i)

# Sum of number 

# sum = 0
# for i in range(1,11):
#     sum += i
# print("sum from 1 to 10 : ", sum)


# sum = 0
# for i in range(10,0,-2):
#     sum += i
# print("sum from 0 to 10 with difference of 2 number: ", sum)


# For else : (Prime or not using For loop and for else)

# num = int(input("Enter any Number : "))
# flag  =1

# n = int(math.sqrt(num))
# # print(n)
# for i in range(2,n):
#     if(num%i==0):
#         flag = 0
#         break

# if flag == 1:
#     print("It's a Prime number")
# else:
#     print("It's not a prime number")


# for i in range(2,n):
#     if(num%i==0):
#         print("It's not a prime number")
#         break
# else:
#     print("It's a prime number")


# Draw patter using for loop:

# for i in range(1, 11):
#     for j in range(1,i+1):
#         print("@", end=" __ ")
#     print("\n")


for i in range(0, 6):
    for j in range(1,i+1):
        if i %2 == 0:
            print("#", end=" ")
        else:
            print("@", end=" ")

    print("\n")