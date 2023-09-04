import math
# List
# my_list = [5,6,1,7,3,0,2,8,4]
# my_list.pop()
# del my_list[1]
# my_list.remove(7)
# print(my_list.index(1))
# my_list.sort()
# my_list.reverse()
# print(my_list)
# list = []
# n =(int(input("Enter the length of array: ")))
# print(n)
# for i in range(n):
#     print("Enter number at Index ", i ," = ",end= " ")
#     a = int(input())

#     list.append(a)

# print(list)
# powerOfTwo = []
# for i in range(11):
#     powerOfTwo.append(2**i)

# print(powerOfTwo)

# comprehension 
# pow = [2 ** x for x in range(11)]
# print(pow)

# print([x+y for x in ['Python', 'java'] for y in [' Language', ' Programming']])

# membership operators:
# list = [1,2,3,4,5,6,7,8,9]
# print(1 in list)
# print('1' in list)


# permutation: 
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
factorialOfN = 1
factorialOfR = 1

for i in range(1,n+1,1):
    factorialOfN *= i
    

for i in range(1,(n-r+1),1):
    factorialOfR *= i 

ncr = factorialOfN/factorialOfR

print("Permutaion of given number : " ,ncr)