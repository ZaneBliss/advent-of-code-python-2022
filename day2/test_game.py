import unittest

from day2 import solution
from day2.fair_game import FairGame
from day2.fixed_game import FixedGame


class TestFairGame(unittest.TestCase):
    def test_call_sample(self):
        fair_game = FairGame()
        self.assertEqual(15, fair_game.call('sample.txt'))

    def test_call_actual(self):
        fair_game = FairGame()
        self.assertEqual(11063, fair_game.call('input.txt'))


class TestFixedGame(unittest.TestCase):
    def test_call_sample(self):
        fixed_game = FixedGame()
        self.assertEqual(12, fixed_game.call('sample.txt'))

    def test_call_actual(self):
        fixed_game = FixedGame()
        self.assertEqual(10349, fixed_game.call('input.txt'))

