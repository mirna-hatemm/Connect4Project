import math
import random
from copy import deepcopy

class Connect4AI:
    def __init__(self, depth):
        self.depth = depth

    def evaluate_position(self, board, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores):
        score = 0

        # Evaluate rows
        for row in range(board.row_count):
            for col in range(board.column_count - board.window_length + 1):
                window = board.grid[row][col:col+board.window_length]
                score += self.get_window_score(window, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)

        # Evaluate columns
        for col in range(board.column_count):
            column = [board.grid[row][col] for row in range(board.row_count)]
            for row in range(board.row_count - board.window_length + 1):
                window = column[row:row+board.window_length]
                score += self.get_window_score(window, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)

        # Evaluate diagonals (top-left to bottom-right)
        for row in range(board.row_count - board.window_length + 1):
            for col in range(board.column_count - board.window_length + 1):
                window = [board.grid[row+i][col+i] for i in range(board.window_length)]
                score += self.get_window_score(window, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)

        # Evaluate diagonals (bottom-left to top-right)
        for row in range(board.row_count - 1, board.window_length - 2, -1):
            for col in range(board.column_count - board.window_length + 1):
                window = [board.grid[row-i][col+i] for i in range(board.window_length)]
                score += self.get_window_score(window, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)

        return score

    def get_window_score(self, window, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores):
        ai_count = window.count(ai_turn)
        player_count = window.count(player_turn)
        empty_count = window.count(empty)

        score = 0
        if ai_count == 4 or (ai_count == 3 and empty_count == 1) or (ai_count == 2 and empty_count == 2):
            score += positive_position_scores[ai_count - 1]
        if player_count == 3 and empty_count == 1:
            score += negative_position_scores[player_count - 1]

        return score

    def minimax(self, board, depth, maximizing_player, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores):
        if depth == 0 or board.check_win():
            if board.check_win():
                if maximizing_player:
                    return -1000000
                else:
                    return 1000000
            else:
                return self.evaluate_position(board, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)

        if maximizing_player:
            value = -float('inf')
            for col in range(board.column_count):
                if board.is_valid_move(col):
                    new_board = deepcopy(board)
                    new_board.make_move(col)
                    value = max(value, self.minimax(new_board, depth-1, False, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores))
            return value
        else:
            value = float('inf')
            for col in range(board.column_count):
                if board.is_valid_move(col):
                    new_board = deepcopy(board)
                    new_board.make_move(col)
                    value = min(value, self.minimax(new_board, depth-1, True, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores))
            return value

    def alphabeta(self, board, depth, alpha, beta, maximizing_player, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores):
        if depth == 0 or board.check_win():
            if board.check_win():
                if maximizing_player:
                    return -1000000
                else:
                    return 1000000
            else:
                return self.evaluate_position(board, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)

        if maximizing_player:
            value = -float('inf')
            for col in range(board.column_count):
                if board.is_valid_move(col):
                    new_board = deepcopy(board)
                    new_board.make_move(col)
                    value = max(value, self.alphabeta(new_board, depth-1, alpha, beta, False, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores))
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break
            return value
        else:
            value = float('inf')
            for col in range(board.column_count):
                if board.is_valid_move(col):
                    new_board = deepcopy(board)
                    new_board.make_move(col)
                    value = min(value, self.alphabeta(new_board, depth-1, alpha, beta, True, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores))
                    beta = min(beta, value)
                    if alpha >= beta:
                        break
            return value

    def get_best_move_minimax(self, board, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores):
        best_move = None
        best_value = -float('inf')
        for col in range(board.column_count):
            if board.is_valid_move(col):
                new_board = deepcopy(board)
                new_board.make_move(col)
                value = self.minimax(new_board, self.depth - 1, False, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)
                if value > best_value:
                    best_value = value
                    best_move = col
        return best_move

    def get_best_move_alphabeta(self, board, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores):
        best_move = None
        best_value = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        for col in range(board.column_count):
            if board.is_valid_move(col):
                new_board = deepcopy(board)
                new_board.make_move(col)
                value = self.alphabeta(new_board, self.depth - 1, alpha, beta, False, ai_turn, player_turn, empty, positive_position_scores, negative_position_scores)
                if value > best_value:
                    best_value = value
                    best_move = col
                alpha = max(alpha, best_value)
        return best_move
