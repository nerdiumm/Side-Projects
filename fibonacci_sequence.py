# Enter a number and have the program generate the Fibonacci sequence to that 
# number OR to the Nth number, whichever occurs first.
# 
# Started: 14 January 2023
# Completed: 14 January 2023

def fibonacci(user_num):
    tracker = 3
    num1 = 0
    num2 = 1
    fib_num = num1 + num2
    print(num1)
    print(num2)
    print(fib_num)
    while (user_num != fib_num) and (tracker != user_num):
        num1 = num2
        num2 = fib_num
        fib_num = num1 + num2
        tracker += 1
        print(fib_num)
    if (user_num == fib_num):
        print("Went to the number you input.")
    else:
        print("Went to the Nth number of the sequence.")

user_inp = input("Enter a number: ")
user_num = int(user_inp)

fibonacci(user_num)