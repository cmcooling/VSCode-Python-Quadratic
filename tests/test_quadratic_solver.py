import unittest
from quadratic_solver import quadratic_solver

##@class TestQuadraticSolver
#A class containing tests for the quadratic_solver function
class TestQuadraticSolver(unittest.TestCase):
    ##Tests if the quadratic and linear coefficients being zero causes a ValeError to be raised
    def test_zero_a_and_b(self):
        with self.assertRaises(ValueError):
            quadratic_solver(0,0,1)

    ##Tests if the correct value is returned when the quadratic coefficient is zero (and the linear coefficient isn't)
    def test_zero_a(self):
        self.assertListEqual(quadratic_solver(0, 1, 2), [-2])

    ##Tests that a single (correct) root is returned when the disriminant is zero
    def test_single_root(self):
        result=quadratic_solver(900,300,25)

        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], 1/6)

