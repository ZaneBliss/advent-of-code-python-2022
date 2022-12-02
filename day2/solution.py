# Part 1

def part_1(file):
    total_score = 0

    with open(file) as f:
        for line in f:
            moves = list(line.strip())
            opponent_move = map_move_to_dict(moves[0])
            _self_move = map_move_to_dict(moves[-1])

            total_score += calculate_score(opponent_move, _self_move)

    return total_score


def calculate_score(opponent_move, _self_move):
    move_score = _self_move['score']
    round_score = 0

    if _self_move['action'] == 'rock':
        if opponent_move['action'] == 'rock':
            round_score = 3
        if opponent_move['action'] == 'paper':
            round_score = 0
        if opponent_move['action'] == 'scissors':
            round_score = 6
    if _self_move['action'] == 'paper':
        if opponent_move['action'] == 'rock':
            round_score = 6
        if opponent_move['action'] == 'paper':
            round_score = 3
        if opponent_move['action'] == 'scissors':
            round_score = 0
    if _self_move['action'] == 'scissors':
        if opponent_move['action'] == 'rock':
            round_score = 0
        if opponent_move['action'] == 'paper':
            round_score = 6
        if opponent_move['action'] == 'scissors':
            round_score = 3

    return move_score + round_score


def map_move_to_dict(move):
    if move == 'A' or move == 'X':
        return {'action': 'rock', 'score': 1}
    elif move == 'B' or move == 'Y':
        return {'action': 'paper', 'score': 2}
    else:
        return {'action': 'scissors', 'score': 3}
