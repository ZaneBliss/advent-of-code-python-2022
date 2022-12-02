import unittest

from day2 import solution
from day2.game import Game


class TestGame(unittest.TestCase):
    def test_run_game_sample(self):
        game = Game()
        self.assertEqual(15, game.run_game('sample.txt'))

    def test_run_game_actual(self):
        game = Game()
        self.assertEqual(11063, game.run_game('input.txt'))

    def test_part2_sample(self):
        self.assertEqual(12, solution.part_2('sample.txt'))

    def test_part2_actual(self):
        self.assertEqual(10349, solution.part_2('input.txt'))

