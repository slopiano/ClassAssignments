# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
        self.assertEqual(classifyTriangle(33,56,65),'Right','33,56,65 is a Right triangle')
        self.assertEqual(classifyTriangle(65,72,97),'Right','5,72,97 is a Right triangle')
        self.assertEqual(classifyTriangle(16,63,65),'Right','16,63,65 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        self.assertEqual(classifyTriangle(65,33,56),'Right','65,33,56 is a Right triangle')
        self.assertEqual(classifyTriangle(73,55,48),'Right','73,55,48 is a Right triangle')
        self.assertEqual(classifyTriangle(55,48,73),'Right','55,48,73 is a Right triangle')
        self.assertEqual(classifyTriangle(77,36,85),'Right','77,36,85 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        side = 5
        self.assertEqual(classifyTriangle(side,side,side),'Equilateral', str(side) + ',' + str(side) + ',' + str(side) + ', should be equilateral')
        side = 200
        self.assertEqual(classifyTriangle(side,side,side),'Equilateral', str(side) + ',' + str(side) + ',' + str(side) + ', should be equilateral')
        side = 2
        self.assertEqual(classifyTriangle(side,side,side),'Equilateral', str(side) + ',' + str(side) + ',' + str(side) + ', should be equilateral')
        side = 34
        self.assertEqual(classifyTriangle(side,side,side),'Equilateral', str(side) + ',' + str(side) + ',' + str(side) + ', should be equilateral')
        side = 22
        self.assertEqual(classifyTriangle(side,side,side),'Equilateral', str(side) + ',' + str(side) + ',' + str(side) + ', should be equilateral')
        side = 67
        self.assertEqual(classifyTriangle(side,side,side),'Equilateral', str(side) + ',' + str(side) + ',' + str(side) + ', should be equilateral')
    
    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(3,5,7),'Scalene')
        self.assertEqual(classifyTriangle(67,4,64),'Scalene')
        self.assertEqual(classifyTriangle(5,4,2),'Scalene')
        self.assertEqual(classifyTriangle(2,4,5),'Scalene')
        self.assertEqual(classifyTriangle(33,4,30),'Scalene')
    
    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isosceles')
        self.assertEqual(classifyTriangle(5,5,9),'Isosceles')
        self.assertEqual(classifyTriangle(9,4,9),'Isosceles')
        self.assertEqual(classifyTriangle(100,150,100),'Isosceles')
        self.assertEqual(classifyTriangle(139,100,100),'Isosceles')
    
    def testOutOfBounds(self): 
        self.assertEqual(classifyTriangle(400,400,400),'InvalidInput')
        self.assertEqual(classifyTriangle(201,200,2),'InvalidInput')
        self.assertEqual(classifyTriangle(200,210,2),'InvalidInput')
        self.assertEqual(classifyTriangle(200,200,210),'InvalidInput')
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput')
        self.assertEqual(classifyTriangle(1.1,1.1,1.1),'InvalidInput')
    
    def testNotTriangle(self): 
        self.assertEqual(classifyTriangle(200,2,2),'NotATriangle')
        self.assertEqual(classifyTriangle(10,150,20),'NotATriangle')
        self.assertEqual(classifyTriangle(10,20,150),'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

