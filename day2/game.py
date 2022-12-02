from day2.paper import Paper
from day2.rock import Rock
from day2.scissors import Scissors


class Game:
    def __init__(self):
        self.total_score = 0

    def run_game(self, file):
        with open(file) as f:
            for line in f:
                moves = list(line.strip())
                opponent_move = self.build_move(moves[0])
                self_move = self.build_move(moves[-1])

                self.total_score += self.calculate_score(opponent_move, self_move)

        return self.total_score

    @classmethod
    def build_move(cls, move):
        if move == 'A' or move == 'X':
            return Rock
        elif move == 'B' or move == 'Y':
            return Paper
        else:
            return Scissors

    @classmethod
    def calculate_score(cls, opponent_move, self_move):
        move_score = self_move.value
        round_score = 0

        if self_move.is_win(opponent_move):
            round_score += 6
        elif self_move.is_loss(opponent_move):
            round_score += 0
        else:
            round_score += 3

        return move_score + round_score
