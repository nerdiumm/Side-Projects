# Program a simple calculator to do basic operators.
# 
# Started: 09 February 2023
# Completed: 3 March 2023

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Can't divide by 0"
    else:
        return num1 / num2

def main():
    print("- Select Operation -")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiple")
    print("4. Divide")
    
    while True:
        choice = input("Enter number choice: ")
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
            
            next_calculation = input("Another calculation? (yes/no): ").lower()
            if next_calculation == "no":
                break
        else:
            print("Invalid Input.")

if __name__ == '__main__':
    main()