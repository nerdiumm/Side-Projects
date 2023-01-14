# User enter a number. Generate PI up to that many decimal places.
# REMEMBER THE LIMITS OF HOW FAR THE PROGRAM CAN GO!
# 
# Started: 13 January 2023
# Completed: 14 January 2023

import math

user_inp = input("How many decimals places would you like to see in PI? ")
deci_places = int(user_inp)

# I stopped at the 49th decimal point because after this, Python just adds zeros
# to the end of pi
if (deci_places <= 48):
    str_format = "%." + user_inp + "f"
    print(str_format % math.pi)
else:
    print("I cannot go that far out into PI.")