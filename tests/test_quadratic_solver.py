import unittest
from quadratic_solver import quadratic_solver

class TestQuadraticSolver(unittest.TestCase):
    def test_zero_a_and_b(self):
        with self.assertRaises(ValueError):
            quadratic_solver(0,0,1)

    def test_zero_a(self):
        self.assertListEqual(quadratic_solver(0, 1, 2), [2])

    def test_single_root(self):
        result=quadratic_solver(900,300,25)

        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0], 1/6)

