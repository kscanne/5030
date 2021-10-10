import unittest
from triangle import is_valid_triangle,traingle_type

class TestTriangle(unittest.TestCase):
    def test_triangle_valid(self):
        result = is_valid_triangle(3,3,3)
        self.assertEqual(type(result),bool)

    def test_return_string(self):
        result = traingle_type(3,3,3)
        self.assertEqual(type(result),str)
    
    def test_return_equilateral(self):
        result = traingle_type(3,3,3)
        self.assertEqual(result,'equilateral')

    def test_return_scalene(self):
        result = traingle_type(3,4,5)
        self.assertEqual(result,'scalene')

    def test_return_isosceles(self):
        result = traingle_type(3,3,2)
        self.assertEqual(result,'isosceles')
    
