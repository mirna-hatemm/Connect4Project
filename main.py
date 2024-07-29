import random
from copy import deepcopy
from Connect4 import Connect4
from Connect4AI import Connect4AI
from randomai import RandomAI

if __name__ == '__main__':
    while True:
        ai_depth = int(input("Choose AI depth (an integer between 1 and 10): "))
        ai_mode = input("Choose AI mode ('alphabeta' or 'minimax'): ")

        board = Connect4()
        ai = Connect4AI(depth=ai_depth)
        random_ai = RandomAI()

        print("Welcome to Connect 4!")
        board.print_board()

        while not board.check_win() and not board.is_board_full():
            print("Random AI is thinking...")
            col = random_ai.get_best_move(board)
            board.make_move(col)
            print(f"Random AI chooses column {col}.")
            board.print_board()

            if not board.check_win() and not board.is_board_full():
                print("AI is thinking...")
                if ai_mode == 'alphabeta':
                    col = ai.get_best_move_alphabeta(board, ai_turn=Connect4.AI_TURN, player_turn=Connect4.PLAYER_TURN,
                                           empty=Connect4.EMPTY, positive_position_scores=Connect4.POSITIVE_POSITION_SCORES,
                                           negative_position_scores=Connect4.NEGATIVE_POSITION_SCORES)
                elif ai_mode == 'minimax':
                    col = ai.get_best_move_minimax(board, ai_turn=Connect4.AI_TURN, player_turn=Connect4.PLAYER_TURN,
                                           empty=Connect4.EMPTY, positive_position_scores=Connect4.POSITIVE_POSITION_SCORES,
                                           negative_position_scores=Connect4.NEGATIVE_POSITION_SCORES)
                else:
                    print("Invalid AI mode. Defaulting to alphabeta.")
                    col = ai.get_best_move(board, ai_turn=Connect4.AI_TURN, player_turn=Connect4.PLAYER_TURN,
                                           empty=Connect4.EMPTY, positive_position_scores=Connect4.POSITIVE_POSITION_SCORES,
                                           negative_position_scores=Connect4.NEGATIVE_POSITION_SCORES)
                board.make_move(col)
                print(f"AI chooses column {col}.")
                board.print_board()

        # Print game result
        if board.check_win():
            if board.current_player == 'X':
                print("Congratulations! O wins!")
            else:
                print("Congratulations! X wins!")
        else:
            print("Game ends in a draw.")

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
