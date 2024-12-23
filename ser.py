def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Cannot divide by zero"

def get_input():
    try:
        return float(input("Enter a number: "))
    except ValueError:
        return "Invalid input"

def show_result(operation, result):
    print(f"The result of {operation} is: {result}")

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
if choice not in ['1', '2', '3', '4']:
    print("Invalid input")
else:
    num1 = get_input()
    if isinstance(num1, str):
        print(num1)  
    else:
        num2 = get_input()
        if isinstance(num2, str):
            print(num2)  
        else:
            if choice == '1':
                show_result("Addition", add(num1, num2))
            elif choice == '2':
                show_result("Subtraction", subtract(num1, num2))
            elif choice == '3':
                show_result("Multiplication", multiply(num1, num2))
            elif choice == '4':
                show_result("Division", divide(num1, num2))
