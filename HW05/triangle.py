"""Module that allows sqrt and other math functions"""
import math

def classify_triangle(side_one, side_two, side_three):
    """This method checks whether a triangle is right,
    scalene, iscoceles, or equilateral triangle"""

    if not(isinstance(side_one,int) and isinstance(side_two,int) and isinstance(side_three,int)) \
        or max(side_one,side_two,side_three) > 200 \
            or min(side_one, side_two, side_three) <= 0:
        return 'InvalidInput'

    if (side_one >= (side_two + side_three)) or \
    (side_two >= (side_one + side_three)) or (side_three >= (side_one + side_two)):
        return 'NotATriangle'

    maximum = max(side_one,side_two,side_three)
    if maximum == side_one:
        total = pow(side_three,2) + pow(side_two,2)
    if maximum == side_two:
        total = pow(side_one,2) + pow(side_three,2)
    if maximum == side_three:
        total = pow(side_one,2) + pow(side_two,2)

    if math.sqrt(total) == maximum:
        return "Right"

    if side_one == side_three or side_one == side_two or side_three == side_two:
        if side_one == side_two and side_one == side_three:
            return "Equilateral"
        return "Isosceles"
    return "Scalene"
