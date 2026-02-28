# random shit to learn basics of python
print("hello world")
a = 10
b = 6
print(a, b)
c = "10.1"
for i in range(a):
    print(i)
    if(i == b):
        break
else:
    print("loop is fully executed")

temp = a
a = b
b = temp
print(a, b)

print(id(a))

d = "junaed"
e = 22
print(d+str(e))

print("name: ", d, "age: ", e)

print("Junaed", "khandakar", sep="-")

print(f"My name is {d} and I am {e} years old")

print("My name is {} and I am {} years old".format(d, e))