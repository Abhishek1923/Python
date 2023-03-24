# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
# Write your code below this line 👇

import math

def paint_calc(height, width, cover):
    number_of_cans = (height * width) / cover
    res=math.ceil(number_of_cans)

    print(f"You'll need {int(res)} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
