# for loops allow us to iterate a set a number of times
# while loops runs until a specific condition is met 

print("="*10)
print("For Loop")
print("="*10)
print()
for loop in range(5):  # range(start, stop, step(increment by))
    print(loop)

print("="*10)
print("For Loop length")
print("="*10)
print()
x = [1,2,3,4]
for loop in range(len(x)):  
    print(x[loop])

print("="*10)
print("For Loop enumerate")
print("="*10)
print()
y = [1,2,3,4]
for loop, element in enumerate(y):  
    print(loop, element)

print("="*10)
print("while loop")
print("="*10)
print()
l = 0 
while l < 5:
    print(l)
    l+= 1

