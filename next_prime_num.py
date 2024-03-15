# Have the program find prime numbers until the user chooses to stop asking for the next one.
# 
# Started: 14 January 2023
# Completed: 14 January 2023

import math

# Function to check whether the user wants the next prime number
def check_user(num_check):
    if(num_check == 0):
        user_inp = input("Would you like to see a prime number?(Y/N) ")
    else:
        user_inp = input("Would like to see the next prime number?(Y/N) ")
    
    if user_inp.capitalize() == 'Y':
        nextPrime(num_check)
    elif user_inp.capitalize() == 'N':
        print("Goodbye!")

# Function to print the next prime number
def nextPrime(num):
    if (isPrime(num)):
        print(num)
        check_user(num+1)
    else:
        nextPrime(num+1)
    pass

# Function to check whether the current number is a prime number
def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    
    if (num % 2 == 0 or num % 3 == 0):
        return False
    
    for i in range(5, int(math.sqrt(num) + 1), 6):
        if (num % i == 0 or num % (i + 2) == 0):
            return False
    
    return True

check_user(0)
