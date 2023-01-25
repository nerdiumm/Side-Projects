# Program converts a decimal number to binary or a binary to it's decimal 
# equivalent.
#
# Started: 19 January 2023
# Completed: XX January 2023

import math

def deciToBin(decimal_num):
    temp = int(decimal_num)
    remainder = -1
    binary = ''

    while temp / 2 != 0:
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = int(temp / 2)
    
    return binary
        

def binToDeci(binary_num):
    temp = str(binary_num)
    power = 0
    result = 0

    while len(temp) > 0:        
        if temp[-1:] == "1":
            result = result + math.pow(2,power)
        
        power += 1
        temp = temp.replace(temp, temp[:-1])
    
    return result

print("15 converted to binary format is %s" % deciToBin(15))
print("1101 converted to decimal format is %d" % binToDeci(1101))
