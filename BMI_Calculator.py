# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Warning you should convert the result to a whole number.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI=float(weight)/(float(height)**2)

print(int(BMI))