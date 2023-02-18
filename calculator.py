# Define function to perform addition operation
def add(num1, num2):
    return num1 + num2

# Define function to perform subtraction operation
def subtract(num1, num2):
    return num1 - num2

# Define function to perform multiplication operation
def multiply(num1, num2):
    return num1 * num2

# Define function to perform division operation
def divide(num1, num2):
    return num1 / num2

# Prompt user for input
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Get user's choice
choice = input("Enter choice (1/2/3/4): ")

# Get user's input for two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operation based on user's choice
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")
