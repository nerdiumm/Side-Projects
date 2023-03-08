# User enter a cost and then the amount given. The program will figure out the 
# change and the number of quarters, dimes, nickels, pennies needed for the change.
#
# Started: 18 January 2023
# Completed: 18 January 2023

import math

def changeCalulate(price, payment):
    # Calculate the amount of change we need to make. Print it out to the user
    temp_difference = int( math.ceil((payment - price) * 100))
    print("Change: $%.2f" % (temp_difference * 0.01))
    # Calculate quarter count
    quarterCount = (temp_difference - (temp_difference % 25)) / 25
    temp_difference = temp_difference % 25
    # Calculate dime count
    dimeCount = (temp_difference - (temp_difference % 10)) / 10
    temp_difference = temp_difference % 10
    # Calculate nickel count
    nickelCount = (temp_difference - (temp_difference % 5)) / 5
    # Calculate penny count
    pennyCount = temp_difference % 5
    # Print out the change and coin count
    print("Your change is in %d quarters, %d dimes, %d nickels, and %d pennies." % (quarterCount, dimeCount, nickelCount, pennyCount))


def checkPayment(price, payment):
    # Check to make see if the payment is less than the price
    # If so, ask for more money
    if (payment < price):
        print("That is not enough to cover the purchase.")
        user_inp = input("Please enter more money: ")
        addedMoney = float(user_inp)
        payment += addedMoney
        checkPayment(price, payment)
    # Check to see if the payment is equal to the price. 
    # If so, no change necessary. Otherwise, payment is greater than the price
    elif payment == price:
        print("Thank you! No change necessary.")
    else:
        changeCalulate(price, payment)

def main():
    # Ask the user for the price of the purchase. Cast into a float
    user_inp = input("Purchase Price: ")
    price = float(user_inp)

    # Ask the user for the amount they gave. Cast into a float
    user_inp = input("How much are you giving? ")
    user_money = float(user_inp)

    checkPayment(price, user_money)

if __name__ == "__main__":
    main()