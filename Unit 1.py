# Lab Exercise 1: Write and execute a basic Python program

print("Welcome to Python Programming!")
name = input("Enter your name: ")
print(f"Hello, {name}! Let's learn Python.")

# Lab Exercise 2: Variables, operators, and input/output

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Output ---")
print("Name:", name)
print("Age:", age)
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")

    # Lab Exercise 3: Simple calculator and area calculation

print("1. Calculator")
print("2. Area calculation")

choice = int(input("Enter your choice: "))

if choice == 1:
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = "Cannot divide by zero" if b == 0 else a / b
    else:
        result = "Invalid operator"

    print("Result:", result)

elif choice == 2:
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    shape = int(input("Choose a shape: "))

    if shape == 1:
        r = float(input("Enter radius: "))
        print("Area of circle:", 3.14159 * r * r)
    elif shape == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of rectangle:", length * width)
    elif shape == 3:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print("Area of triangle:", 0.5 * base * height)
    else:
        print("Invalid shape")

else:
    print("Invalid choice")

# Mini Project: Unit Converter

print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")
print("5. Kilograms to Pounds")
print("6. Pounds to Kilograms")

choice = int(input("Enter your choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print("Miles:", value * 0.621371)
elif choice == 2:
    print("Kilometers:", value * 1.60934)
elif choice == 3:
    print("Fahrenheit:", (value * 9 / 5) + 32)
elif choice == 4:
    print("Celsius:", (value - 32) * 5 / 9)
elif choice == 5:
    print("Pounds:", value * 2.20462)
elif choice == 6:
    print("Kilograms:", value * 0.453592)
else:
    print("Invalid choice")



