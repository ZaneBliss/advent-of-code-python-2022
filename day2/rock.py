class Rock:
    name = 'rock'
    value = 1

    @classmethod
    def is_win(cls, other):
        return True if other.name == 'scissors' else False

    @classmethod
    def is_tie(cls, other):
        return True if other.name == 'rock' else False

    @classmethod
    def is_loss(cls, other):
        return True if other.name == 'paper' else False
