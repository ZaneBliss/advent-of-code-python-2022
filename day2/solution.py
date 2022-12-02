def part_2(file):
    total_score = 0

    with open(file) as f:
        for line in f:
            moves = list(line.strip())
            opponent_move = map_move_to_dict(moves[0])
            outcome = map_outcome_to_dict(moves[-1])

            total_score += calculate_score_for_outcome(opponent_move, outcome)

    return total_score


def map_move_to_dict(move):
    if move == 'A' or move == 'X':
        return {'action': 'rock', 'score': 1}
    elif move == 'B' or move == 'Y':
        return {'action': 'paper', 'score': 2}
    else:
        return {'action': 'scissors', 'score': 3}
