# Write a program that calculates the distance between two cities and
# allows the user to specify a unit of distance. May require finding 
# coordinates for the citie like latitude and longitude.
#
# Started: 07 March 2023
# Completed: 25 April 2023

# Importing the geodesic module from the library
from geopy import distance
from geopy.distance import geodesic

# Function for checking if the user entered city is in our dictionary
def check_city(city, flag_num):
    if city in cities_dict:
        flag_found_key[flag_num] = True
    else:
        print("Try a different city...")

# Function to check if the user entered unit is in our list
def check_unit(unit):
    return True if unit in units_of_dist else False

# Function to calculate the distance using the geodesic function in geopy
# according to the unit the user requested
def calculate_dist():
    if user_unit.lower().__eq__("km") or user_unit.lower().__eq__("kilometers"):
        print("%.3f kilometers" % geodesic(cities_dict[user_cities[0].upper()], cities_dict[user_cities[1].upper()]).km)
    elif user_unit.lower().__eq__("m") or user_unit.lower().__eq__("meters"):
        print("%.3f meters" % geodesic(cities_dict[user_cities[0].upper()], cities_dict[user_cities[1].upper()]).m)
    else:
        print("%.3f miles" % geodesic(cities_dict[user_cities[0].upper()], cities_dict[user_cities[1].upper()]).mi)

# Created dictionary of top 10 major US cities and list of units of distance
cities_dict = {
    "CHICAGO": [25.7617, -80.1918],
    "DALLAS": [32.779167, -96.808891],
    "HOUSTON": [29.749907, -95.358421],
    "LOS ANGELES": [34.052235, -118.243683],
    "NEW YORK": [40.730610, -73.935242],
    "PHILADELPHIA": [39.952583, -75.165222],
    "PHOENIX": [33.448376, -112.074036],
    "SAN ANTONIO": [29.424349, -98.491142],
    "SAN DIEGO": [32.715736, -117.161087],
    "SAN JOSE": [37.335480, -121.893028]
}
units_of_dist = ["km", "kilometers", "m", "meters", "mi", "miles"]

# Created flag array for checking cities and array of user cities
flag_found_key = [False, False]
flag_valid_unit = False
user_cities = ["", ""]

# Loop through both flags and cities arrays to check and change flags accordingly
for x in range(0,2):
    while not flag_found_key[x]:
        user_cities[x] = input("Enter a US city: ")
        check_city(user_cities[x].upper(), x)

# Loop to accept the user's unit of distance and ask for 
# another if the entered unit is invalid
while not flag_valid_unit:
    user_unit = input("Enter a valid unit of measurement: ")
    flag_valid_unit = check_unit(user_unit.lower())

calculate_dist()
