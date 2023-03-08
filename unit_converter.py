# Program that converts various units between one another. User 
# enters the type of unit being entered, the type of unit they want 
# to convert to and then the value. Then the program makes the conversion.
# Convert temp, currency, volume, and mass
# 
# Started: 3 March 2023
# Completed: 3 March 2023

unit_dict = {
    "USD": 1.0,
    "EUR": 0.94185,
    "GBP": 0.83362,
    "cubic meter": 1000.0,
    "cubic centimeter": 0.001,
    "cubic feet": 35.31,
    "millilitre": 0.001,
    "litre": 1.0,
    "gallon": 3.785,
    "gram": 1.0,
    "kilogram": 1000.0,
    "milligram": 0.001,
    "ton": 1000000.0,
    "pound": 453.592,
    "ounce": 28.3495
}

UNIT_SELECTIONS = [
    "celsius",
    "fahrenheit",
    "kelvin",
    "USD",
    "EUR",
    "GBP",
    "cubic meter",
    "cubic centimeter",
    "cubic feet",
    "millilitre",
    "litre",
    "gallon",
    "gram",
    "kilogram",
    "milligram",
    "ton",
    "pound",
    "ounce"
]

temp_units = ["celsius", "fahrenheit"]
currency_units = ["USD", "EUR", "GBP"]
volume_units = ["cubic meter", "cubic centimeter", "millilitre", "litre", "gallon"]
mass_units = ["gram", "kilogram", "milligram", "ton", "pound", "ounce"]

while True:
    input_unit = input("Enter the type of unit you want to convert: ")
    output_unit = input("Enter the type of unit you want to convert into: ")
    
    if input_unit not in UNIT_SELECTIONS:
        print("Invalid input unit. Please try another unit.\n")
        continue
    elif output_unit not in UNIT_SELECTIONS:
        print("Invalid output unit. Please try another unit.\n")
        continue

    input_val_str = input("Enter the value you want to convert: ")
    input_val = float(input_val_str)

    can_convert = [
        input_unit in temp_units and output_unit in temp_units,
        input_unit in currency_units and output_unit in currency_units,
        input_unit in volume_units and output_unit in volume_units,
        input_unit in mass_units and output_unit in mass_units
    ]

    if any(can_convert):
        output_val = 0.0
        if (input_unit == "celsius") and (output_unit == "fahrenheit"):
            output_val = (input_val * 1.8) + 32
        elif (input_unit == "fahrenheit") and (output_unit == "celsius"):
            output_val = (input_val - 32) * (5/9)
        else:
            output_val = (input_val * unit_dict[input_unit] / unit_dict[output_unit])
        
        print("%.2f %s = %.2f %s\n" % (input_val, input_unit, output_val, output_unit))
    else:
        print("Invalid conversion attempt. Try different units.\n")
    
    input_check = input("Would you like to do another conversion? (yes/no): ")
    if (input_check.lower() == "no"):
        break
