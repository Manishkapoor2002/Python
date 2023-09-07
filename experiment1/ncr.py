# p(n, r) = n! / (n-r)!.
n = int(input("Enter The value of n: "))
r = int(input("Enter The value of r: "))

factN = 1
factNminR = 1
for i in range(1,n+1):
    factN *= i

for i in range(1,(n-r+1)):
    factNminR *=  i

npr = factN/factNminR

print(npr)


