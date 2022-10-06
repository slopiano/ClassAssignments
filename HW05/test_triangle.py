# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    """Tests the triangle.py file"""

    def test_right_triangle_a(self):
        """Tests right triangles"""
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5,12,13),'Right','5,12,13 is a Right triangle')
        self.assertEqual(classify_triangle(33,56,65),'Right','33,56,65 is a Right triangle')
        self.assertEqual(classify_triangle(65,72,97),'Right','5,72,97 is a Right triangle')
        self.assertEqual(classify_triangle(16,63,65),'Right','16,63,65 is a Right triangle')

    def test_right_triangle_b(self):
        """Tests right triangles"""
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classify_triangle(65,33,56),'Right','65,33,56 is a Right triangle')
        self.assertEqual(classify_triangle(73,55,48),'Right','73,55,48 is a Right triangle')
        self.assertEqual(classify_triangle(55,48,73),'Right','55,48,73 is a Right triangle')
        self.assertEqual(classify_triangle(77,36,85),'Right','77,36,85 is a Right triangle')

    def test_equilateral_triangles(self):
        """Tests equilateral triangles"""
        side = 5
        self.assertEqual(classify_triangle(side,side,side),\
            'Equilateral', str(side) + ',' + str(side) + ',' + str(side) +\
                ', should be equilateral')
        side = 200
        self.assertEqual(classify_triangle(side,side,side),\
            'Equilateral', str(side) + ',' + str(side) + ',' + str(side) +\
                ', should be equilateral')
        side = 2
        self.assertEqual(classify_triangle(side,side,side),\
            'Equilateral', str(side) + ',' + str(side) + ',' + str(side) +\
                ', should be equilateral')
        side = 34
        self.assertEqual(classify_triangle(side,side,side),\
            'Equilateral', str(side) + ',' + str(side) + ',' + str(side) +\
                ', should be equilateral')
        side = 22
        self.assertEqual(classify_triangle(side,side,side),\
            'Equilateral', str(side) + ',' + str(side) + ',' + str(side) +\
                ', should be equilateral')
        side = 67
        self.assertEqual(classify_triangle(side,side,side),\
            'Equilateral', str(side) + ',' + str(side) + ',' + str(side) +\
                ', should be equilateral')

    def test_scalene_triangles(self):
        """Tests scalene triangles"""
        self.assertEqual(classify_triangle(3,5,7),'Scalene')
        self.assertEqual(classify_triangle(67,4,64),'Scalene')
        self.assertEqual(classify_triangle(5,4,2),'Scalene')
        self.assertEqual(classify_triangle(2,4,5),'Scalene')
        self.assertEqual(classify_triangle(33,4,30),'Scalene')

    def test_isosceles_triangles(self):
        """Tests isosceles triangles"""
        self.assertEqual(classify_triangle(1,2,2),'Isosceles')
        self.assertEqual(classify_triangle(5,5,9),'Isosceles')
        self.assertEqual(classify_triangle(9,4,9),'Isosceles')
        self.assertEqual(classify_triangle(100,150,100),'Isosceles')
        self.assertEqual(classify_triangle(139,100,100),'Isosceles')

    def test_out_bounds(self):
        """Tests if the parameters are valid"""
        self.assertEqual(classify_triangle(400,400,400),'InvalidInput')
        self.assertEqual(classify_triangle(201,200,2),'InvalidInput')
        self.assertEqual(classify_triangle(200,210,2),'InvalidInput')
        self.assertEqual(classify_triangle(200,200,210),'InvalidInput')
        self.assertEqual(classify_triangle(0,0,0),'InvalidInput')
        self.assertEqual(classify_triangle(1.1,1.1,1.1),'InvalidInput')

    def test_not_triangle(self):
        """Tests if the sides can't make a triangle"""
        self.assertEqual(classify_triangle(200,2,2),'NotATriangle')
        self.assertEqual(classify_triangle(10,150,20),'NotATriangle')
        self.assertEqual(classify_triangle(10,20,150),'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
