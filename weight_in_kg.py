import math

weight = input("Enter weight: ")
unit = input("Kg(k) or Lbs(l): ")

if unit == "l" or "L":
    weight = float(weight) / 2.20462
    weight = round(weight, ndigits=1)
    print(f"{weight} Kgs")
elif unit == "k" or "K":
    weight == float(weight) * 2.20462
    weight = round(weight, ndigits=1)
    print(f"{weight} Lbs")
