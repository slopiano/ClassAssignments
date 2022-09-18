import pytest
import math
from triangle import classify_triangle

def test_scalene():
    assert classify_triangle(1,4,2) == "scalene"
    assert classify_triangle(1,2,3) == "scalene"
    assert classify_triangle(4,56,80) == "scalene"
    assert classify_triangle(123124,2424,344) == "scalene"

def test_isoceles():
    assert classify_triangle(7,7,100) == "isoceles"
    assert classify_triangle(67,67,3) == "isoceles"
    assert classify_triangle(1,1,2) == "isoceles"
    assert classify_triangle(8,9,8) == "isoceles"

def test_equilateral():
    a=2
    assert classify_triangle(a,a,a) == "equilateral"
    a=60
    assert classify_triangle(a,a,a) == "equilateral"
    a=90
    assert classify_triangle(a,a,a) == "equilateral"
    a=20
    assert classify_triangle(a,a,a) == "equilateral"
    a=100000000
    assert classify_triangle(a,a,a) == "equilateral"

def test_scalene_right():
    a = 4
    b = 30
    hyp = math.sqrt(math.pow(a,2) + math.pow(b,2))
    assert classify_triangle(a,b,hyp) == "scalene right"
    a = 23452345
    b = 124083498
    hyp = math.sqrt(math.pow(a,2) + math.pow(b,2))
    assert classify_triangle(a,b,hyp) == "scalene right"
    a = 4.346
    b = 30.2352
    hyp = math.sqrt(math.pow(a,2) + math.pow(b,2))
    assert classify_triangle(a,b,hyp) == "scalene right"
    a = 4.984
    b = 243646
    hyp = math.sqrt(math.pow(a,2) + math.pow(b,2))
    assert classify_triangle(a,b,hyp) == "scalene right"

def test_isoceles_right():
    sides = 5
    hypotenuse = math.sqrt(pow(sides,2) + pow(sides,2))
    assert classify_triangle(sides,sides,hypotenuse) == "isoceles right"
    sides = 10
    hypotenuse = math.sqrt(pow(sides,2) + pow(sides,2))
    assert classify_triangle(sides,sides,hypotenuse) == "isoceles right"
    sides = 4
    hypotenuse = math.sqrt(pow(sides,2) + pow(sides,2))
    assert classify_triangle(sides,sides,hypotenuse) == "isoceles right"
    sides = 100
    hypotenuse = math.sqrt(pow(sides,2) + pow(sides,2))
    assert classify_triangle(sides,sides,hypotenuse) == "isoceles right"
    sides = 421098
    hypotenuse = math.sqrt(pow(sides,2) + pow(sides,2))
    assert classify_triangle(sides,sides,hypotenuse) == "isoceles right"

def test_failures():
    sides = 5
    hypotenuse = math.sqrt(pow(sides,2) + pow(sides,2))
    assert classify_triangle(sides,sides,hypotenuse) == "blah"

def test_failures1():
    assert classify_triangle(8,15,17) == "scalene"
    sides = 4
    hypotenuse = math.sqrt(pow(sides,2) + pow(sides,2))

def test_failures2():
    assert classify_triangle(sides,sides,hypotenuse) == "isoceles"

def test_failures3():
    assert classify_triangle(123124,2424,344) == "equilateral"

def test_failures5():
    assert classify_triangle(67,67,3) == "FAILURE"
    