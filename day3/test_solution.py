import unittest

from day3.solution import Solution


class TestSolution(unittest.TestCase):
    def test_part1_sample(self):
        self.assertEqual(157, Solution.part1('sample.txt'))

    def test_part1_actual(self):
        self.assertEqual(8401, Solution.part1('input.txt'))

    def test_part2_sample(self):
        self.assertEqual(70, Solution.part2('sample.txt'))

    def test_part2_sample(self):
        # self.assertEqual(70, Solution.part2('input.txt'))
        Solution.part2('sample.txt')
