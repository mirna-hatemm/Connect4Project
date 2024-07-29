import random
from Connect4 import Connect4

class RandomAI:
    def __init__(self):
        pass

    def get_best_move(self, board):
        valid_moves = board.get_valid_moves()
        return random.choice(valid_moves)
