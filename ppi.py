#!/usr/bin/env python3

import math


def CalculatePi(roundVal):

    somepi = round(math.pi, roundVal)
    return somepi


roundTo = input("Enter the number of digits you want after the decimal for Pi: ")
try:
    roundint = int(roundTo)
    print(CalculatePi(roundint))
except:
    print("You did not enter an integer")
