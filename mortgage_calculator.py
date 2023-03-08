# Calculate the montly payments of a fixed term mortgage over given Nth terms 
# at a given interest rate. Also, figure out how long it will take the user to 
# pay back the loan.
# Added Complexity: add an option for users to select the compounding interval
# (monthly, weekly, daily, continually)
# 
# Started: 15 January 2023
# Completed: XX January 2023

import math
# Ask the user for the value of the mortgage
user_inp = input("What is the value of the mortgage? ")
mortgage_val = float(user_inp)

# Ask the user for the interest rate
user_inp = input("What is the interest rate? ")
interest_rate = float(user_inp)

# Ask the user the number of months of the loan
user_inp = input("How many months is the mortgage good for? ")
term_length = int(user_inp)

# Calculate the monthly payments
monthly_interest_rate = float((interest_rate / 100) / 12)
print("Monthly Interest Rate: %f" % monthly_interest_rate)
monthly_interest_rate1 = float(1 + monthly_interest_rate)
monthly_payments = float((mortgage_val * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, term_length)) / ( (math.pow(1 + monthly_interest_rate, term_length)) - 1 )))

# Print the monthly payments
print("Monthly Payments: $%.2f" % monthly_payments)
