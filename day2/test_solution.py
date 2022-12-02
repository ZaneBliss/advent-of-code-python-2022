import unittest

from day2 import solution


class TestSolution(unittest.TestCase):
    def test_part1_sample(self):
        self.assertEqual(15, solution.part_1('sample.txt'))

    def test_part1_actual(self):
        self.assertEqual(11063, solution.part_1('input.txt'))

