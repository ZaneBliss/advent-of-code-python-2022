from day2.game import Game


class FixedGame(Game):
    def __int__(self):
        self.total_score = 0

    @classmethod
    def call(cls, file):
        total_score = 0

        with open(file) as f:
            for line in f:
                moves = list(line.strip())
                opponent_move = Game.build_move(moves[0])
                outcome = cls.map_outcome_to_dict(moves[-1])

                total_score += cls.calculate_score_for_outcome(opponent_move, outcome)

        return total_score

    @classmethod
    def calculate_score_for_outcome(cls, opponent_move, outcome):
        round_score = outcome['score']
        move_score = 0

        if outcome['status'] == 'loss':
            if opponent_move.name == 'rock':
                move_score = 3
            if opponent_move.name == 'paper':
                move_score = 1
            if opponent_move.name == 'scissors':
                move_score = 2
        if outcome['status'] == 'tie':
            move_score = opponent_move.value
        if outcome['status'] == 'win':
            if opponent_move.name == 'rock':
                move_score = 2
            if opponent_move.name == 'paper':
                move_score = 3
            if opponent_move.name == 'scissors':
                move_score = 1

        return move_score + round_score

    @classmethod
    def map_outcome_to_dict(cls, outcome):
        if outcome == 'X':
            return {'status': 'loss', 'score': 0}
        elif outcome == 'Y':
            return {'status': 'tie', 'score': 3}
        else:
            return {'status': 'win', 'score': 6}

