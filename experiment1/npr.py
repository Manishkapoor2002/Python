# c(n, r) = n! / (r!*(n-r)!) = p(n,r)

n = int(input("Enter The value of n: "))
r = int(input("Enter The value of r: "))

factN = 1
factNminR = 1
factR = 1
for i in range(1,n+1):
    factN *= i
for i in range(1,r+1):
    factR *= i

for i in range(1,(n-r+1)):
    factNminR *=  i

ncr = factN/(factNminR*factR)

print(ncr)