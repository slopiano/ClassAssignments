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
    assert classify_triangle(8,6,10) == "scalene right"
    assert classify_triangle(3,4,5) == "scalene right"
    assert classify_triangle(21,20,29) == "scalene right"
    assert classify_triangle(8,15,17) == "scalene right"

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