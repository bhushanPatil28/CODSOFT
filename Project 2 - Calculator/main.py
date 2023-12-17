print("----------------Welcome to simple PYTHON calculator----------------")
choice = int(input("Enter 0 for help or 1 to continue: "))
print()

if choice == 0:
    print("Enter number 1 and then number 2\nthen select what operation do you want to perform!")

number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

operation = input("Enter the operation you want to perform(+,-,/,*)) :")

if operation == '+':
    print(f"Result: {number1+number2}")
elif operation == '-':
    print(f"Result: {number1-number2}")
elif operation == '/':
    print(f"Result: {number1/number2}")
elif operation == '*':
    print(f"Result: {number1*number2}")
else:
    print("Entered operation is not supported!")

