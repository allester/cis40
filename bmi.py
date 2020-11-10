"""
Lab 3 - bmi.py - De Anza  CIS D040 - Allester Ramayrat
"""

def bmi(inches,lbs):

    bmi = (lbs / inches ** 2) * 703

    if bmi >= 30:
        category = "Obese"

    if bmi < 30:
        category = "Overweight"

    if bmi < 25:
        category = "Normal weight"

    if bmi < 18.5:
        category = "Underweight"

    print("BMI =", bmi, ":", category)

inches = float(input("Enter your height in inches, including decimal fractional parts: "))

lbs = int(input("Enter your weight in pounds: "))

bmi(inches,lbs)