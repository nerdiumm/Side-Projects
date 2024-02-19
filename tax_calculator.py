# Program that asks the user to enter a cost and either a country or state tax. 
# Return the tax plus the total cost with tax
# 
# Using the state sales tax rate for each state found here: 
# https://www.rocketmoney.com/learn/personal-finance/sales-tax-by-state
# Using the top 10 (excluding the US) countries with the highest population's
# sales tax numbers. Tax rates found here:
# https://take-profit.org/en/statistics/sales-tax-rate/#continents
# 
# Started: 25 April 2023
# Completed: XX February 2024


# Function to check if the arg country is a valid country in dictionary
# or is the United States
def country_check(country):
    if country.upper() in country_taxes:
        return True
    elif country.upper().__eq__("UNITED STATES") or country.upper().__eq__("US") or country.upper().__eq__("USA"):
        return True
    else:
        print("Invalid country. Try again...\n")
        return False

# Function to check if the arg country is the United States
def USA_check(country):
    if country.upper().__eq__("UNITED STATES") or country.upper().__eq__("US") or country.upper().__eq__("USA"):
        return True
    else:
        return False

# Function to check if the arg state is a valid US state
def state_check(state):
    if state.upper() in state_taxes:
        return True
    else:
        return False

# Function to check if the arg purchase can be cast as a float without error
def check_purchase(purchase):
    try:
        float(purchase)
        return True
    except ValueError:
        return False

# Function to return the state the user enters their purchase is from.
# Loops until a valid state is entered
def get_state():
    user_state = input("Enter what state your purchase is in: ")
    while not state_check(user_state.upper()):
        print("Not a valid US state.")
        user_state = input("Enter what state your purchase is in: ")
    
    return user_state.upper()

# Function to return the tax of the given country or US state
# Calls get_state() to grab the US state to return
def get_tax(country):
    if country.upper().__eq__("UNITED STATES") or country.upper().__eq__("US") or country.upper().__eq__("USA"):
        us_state = get_state()
        return state_taxes[us_state.upper()]
    else:
        return country_taxes[country.upper()]

# Function to calculate total purchase given args subtotal and tax
def get_total_purchase(subtotal, tax):
    return subtotal + (subtotal * (tax/100))

# Created dictionaries for the sales taxes for the individual states in the US 
# and the other top 9 highly populated countries
state_taxes = {
    "ALABAMA": 4.00,
    "ALASKA": 0,
    "ARIZONA": 5.60,
    "ARKANSAS": 6.50,
    "CALIFORNIA": 7.25,
    "COLORADO": 2.90,
    "CONNECTICUT": 6.35,
    "D.C.": 6.00,
    "FLORIDA": 6.00,
    "GEORGIA": 4.00,
    "HAWAII": 4.00,
    "IDAHO": 6.00,
    "ILLINOIS": 6.25,
    "INDIANA": 7.00,
    "IOWA": 6.00,
    "KANSAS": 6.50,
    "KENTUCKY": 6.00,
    "LOUISIANA": 4.45,
    "MAINE": 5.50,
    "MARYLAND": 6.00,
    "MASSACHUSETTS": 6.25,
    "MICHIGAN": 6.00,
    "MINNESOTA": 6.88,
    "MISSISSIPPI": 7.00,
    "MISSOURI": 4.23,
    "NEBRASKA": 5.50,
    "NEVADA": 6.85,
    "NEW JERSEY": 6.63,
    "NEW MEXICO": 5.00,
    "NEW YORK": 4.00,
    "NORTH CAROLINA": 4.75,
    "NORTH DAKOTA": 5.00,
    "OHIO": 5.75,
    "OKLAHOMA": 4.50,
    "PENNSYLVANIA": 6.00,
    "RHODE ISLAND": 7.00,
    "SOUTH CAROLINA": 6.00,
    "SOUTH DAKOTA": 4.50,
    "TENNESSEE": 7.00,
    "TEXAS": 6.25,
    "UTAH": 6.10,
    "VERMONT": 6.00,
    "VIRGINIA": 5.30,
    "WASHINGTON": 6.50,
    "WEST VIRGINIA": 6.00,
    "WISCONSIN": 5.00,
    "WYOMING": 4.00
}
country_taxes = {
    "CHINA": 13,
    "INDIA": 18,
    "INDONESIA": 11,
    "PAKISTAN": 17,
    "NIGERIA": 7.5,
    "BRAZIL": 17,
    "BANGLADESH": 15,
    "RUSSIA": 20,
    "MEXICO": 16
}

# Created flags to know if country is valid and if the country is the USA
flag_valid_country = False
flag_is_USA = False
tax = 0.0

# Gather user input for the purchase total
user_input = input("Enter how much your purchase is: ")
while not check_purchase(user_input):
    print("\nNot a valid purchase quantity")
    user_input = input("Enter how much your purchase is: ")

# Conver the input from str to float
purchase = float(user_input)

# Loop until user enters a valid country in our list OR the United States
# Change flag var to True when found
while not flag_valid_country:
    user_country = input("Enter the country your purchase is in: ")
    flag_valid_country = country_check(user_country.upper())
    flag_is_USA = USA_check(user_country.upper())

# Find the tax for the given country or US state
tax = get_tax(user_country)

# Print out final purchase total and the tax percentage
print("Tax = %.2f%%" % (tax))
print("Purchase total: $%.2f" % get_total_purchase(purchase, tax))
