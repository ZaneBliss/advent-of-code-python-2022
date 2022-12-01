import unittest
from day1.expedition import Expedition


class TestExpedition(unittest.TestCase):
    def test_elf_with_most_calories_sample(self):
        expedition = Expedition()

        expedition.load_elves_from_file('sample.txt')
        elf = expedition.elf_with_most_calories()

        self.assertEqual(24000, elf.total_calories_of_inventory())

    def test_elf_with_most_calories_actual(self):
        expedition = Expedition()

        expedition.load_elves_from_file('input.txt')
        elf = expedition.elf_with_most_calories()

        self.assertEqual(69693, elf.total_calories_of_inventory())

    def test_sum_calories_for_top_elves_sample(self):
        expedition = Expedition()

        expedition.load_elves_from_file('sample.txt')

        self.assertEqual(45000, expedition.sum_calories_for_top_elves())

    def test_sum_calorie_for_top_elves_actual(self):
        expedition = Expedition()

        expedition.load_elves_from_file('input.txt')

        self.assertEqual(200945, expedition.sum_calories_for_top_elves())
