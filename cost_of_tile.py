# Have the program calculate the total cost of tile it would take to cover 
# a floor plan of x width and y height, using a cost entered by the user.
# 
# Started: 15 January 2023
# Completed: XX January 2023

user_inp = input("How much do the tiles cost? ")
tile_price = float(user_inp)

user_inp = input("What is the width of the area you're tiling? ")
area_width = float(user_inp)

user_inp = input("What is the height of the area you're tiling? ")
area_height = float(user_inp)

total_price = float(tile_price * (area_height * area_width))
print("Total price for the area: $%.2f" % total_price)