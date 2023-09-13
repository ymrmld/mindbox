import unittest
from square import Square
from math import pi, sqrt

class TestSquareArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Square(3, 4, 5), f'S(прямоугольного треугольника) = {0.5*3*4}')
        self.assertEqual(Square(3, 4, 4), f'S(треугольника) = {0.5*sqrt(13.75)*3}')
        self.assertEqual(Square(3), f'S(круга) = {3*3*pi}')
    
    def test_values(self):
        self.assertRaises(ValueError, Square, -3, 2, 1)
        self.assertRaises(ValueError, Square, 0, 0, 1)
        self.assertRaises(ValueError, Square, -3, '2i', 1)
        self.assertRaises(ValueError, Square, 3, '2i', 1)
        self.assertRaises(ValueError, Square, [3,2,1], '2i', 1)
        self.assertRaises(ValueError, Square, 1, 2, 3)

        self.assertRaises(ValueError, Square, -3)
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, 'q')
        self.assertRaises(ValueError, Square, [1, 2, 3])
