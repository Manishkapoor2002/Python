temp = 2
count = 0
for i in range(3,1000):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        if((i - temp )== 2):
            print("(",end="")
            print(temp,",",i,end="")
            print("), ",end="")

            count = count + 1

        temp = i
print(count)

        