age = 25
has_ID = True

if age >= 19 and has_ID == True: 
    print("Allow to enter")
else:
    print("Entry denied")

a = "hello"
b = "hello"

if (a is b): # If object are same
    print("same")

if (a == b): # If value are same
    print("same")

print("same" if (a == b) else "not same") # Ternary operator

for i in range(10): # range(stop)
    print(i)

for i in range(1, 10, 1): # range(start, stop, step)
    print(i)

for i in range(1, 10): # range(start, stop)
    print(i)

for i in range(10): # range(stop)
    print(i)

n = 5
for i in range(n):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(1, n*i):
    print("*", end=" ")


#fibbonacchi series
a = 0
b = 1
num = int(input("Enter the number: "))
print(a, b, end=" ")
for i in range(num):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylist)

print(mylist[2:5])

print(mylist[-2:9])
