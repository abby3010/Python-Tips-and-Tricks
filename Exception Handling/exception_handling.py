# Try and Except in Python

try:
    age = int(input("Enter your age"))
    print("Your age is " , age)
except Exception as e:
    print("Check your input")
finally:
    print("Finally I'll run")

print("Important Code")