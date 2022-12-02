from day2.paper import Paper
from day2.rock import Rock
from day2.scissors import Scissors


class Game:
    @classmethod
    def build_move(cls, move):
        if move == 'A' or move == 'X':
            return Rock
        elif move == 'B' or move == 'Y':
            return Paper
        else:
            return Scissors


