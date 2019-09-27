import unittest
from quadratic_solver import quadratic_solver

class TestQuadraticSolver(unittest.TestCase):
    def test_zero_a_and_b(self):
        with self.assertRaises(ValueError):
            quadratic_solver(0,0,1)

    def test_zero_a(self):
        self.assertListEqual(quadratic_solver(0, 1, 2), [2])

