import math

def classify_triangle(a, b, c):
    right = ""
    maximum = max(a,b,c)
    if(maximum == a):
        total = pow(c,2) + pow(b,2)
    if(maximum == b):
        total = pow(a,2) + pow(c,2)
    if(maximum == c):
        total = pow(a,2) + pow(b,2)

    if(math.sqrt(total) == maximum):
        right = " right"
    
    if(a == c or a == b or c == b):
        if(a == b and a == c):
            return "equilateral"
        else:
            return "isoceles" + right
    else:
        return "scalene" + right
