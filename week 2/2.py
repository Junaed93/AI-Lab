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
