# User enters a number. Have the program find all Prime Factors (if there are any) and 
# display them.
# 
# Started: 14 January 2023
# Completed: 14 January 2023

# Function to find the prime factors of user input number
def prime_factorization(num):
    # A list to keep track of prime factors
    prime_factors = []
    # int variable to hold factorized number and to check when we reach 1 or a prime number
    factorized_num = num

    # While loop to check when we hit 1
    while factorized_num != 1:
        # For loop to go through prime numbers since user number can be any size.
        # Will break out of for loop when we find the smallest prime number that can 
        # divided into user's num
        for x in range(2,num):
            if factorized_num % x == 0:
                prime_factors.append(x)
                factorized_num = factorized_num / x
                break
    # Print prime factors list for user's num
    print("Prime Factors of", num, ":",prime_factors)

# Ask user for number and cast it into an integer
user_inp = input("Enter a number: ")
user_num = int(user_inp)
# Call prime factorization method with user's number
prime_factorization(user_num)