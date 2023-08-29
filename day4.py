# Jumping Statements:
# Break statement:
print("Using Break : ")

for i in range(1,10):
    if i == 5:
        break
    print(i ,end=" ")

print()
print()

# continue
print("Using continue : ")
for i in range(1,10):
    if i == 5:
        continue
    print(i,end=" ")

print()
print()

# Pass
print("Using Pass:")
for i in range(1,10):
    if i == 5:
        pass
    print(i ,end=" ")