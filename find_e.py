# User enters a number. Generate e to the power of that number.
# REMEMBER THE LIMITS OF HOW FAR THE PROGRAM CAN GO!
# 
# Started: 14 January 2023
# Completed: 14 January 2023

import math

user_inp = input("How many deciaml places would you like the math constant e? ")
pwr = int(user_inp)

# I stopped at the 51st decimal point because after this, Python adds zeroes to
# the end of the e.
if pwr <= 51:
    str_format = "%." + user_inp + "f"
    print(str_format % math.e)
else:
    print("I cannt go that far out into e.")