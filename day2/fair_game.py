from day2.game import Game


class FairGame(Game):
    def __init__(self):
        self.total_score = 0

    def call(self, file):
        with open(file) as f:
            for line in f:
                moves = list(line.strip())
                opponent_move = self.build_move(moves[0])
                self_move = self.build_move(moves[-1])

                self.total_score += self.calculate_score(opponent_move, self_move)

        return self.total_score

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
