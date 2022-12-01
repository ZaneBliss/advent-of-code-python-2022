import unittest
import solution


class TestSolution(unittest.TestCase):
    def test_part_1(self):
        self.assertEqual(69693, max(solution.calories_per_elf("input.txt")))

    def test_part_2(self):
        calorie_list = solution.calories_per_elf("input.txt")

        self.assertEqual(200945, solution.sum_top_three(calorie_list))
