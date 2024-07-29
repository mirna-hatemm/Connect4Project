import math
import time

import matplotlib.pyplot as plt

from Connect4 import Connect4
from Connect4AI import Connect4AI


def measure_algorithm_performance(algorithm, depth):
    total_time = 0

    for _ in range(10):  # Repeat the measurement multiple times for better accuracy
        board = Connect4()  # Create a new Connect4 board
        ai = Connect4AI(depth)  # Create a new Connect4AI instance with the specified depth

        start_time = time.time()
        if algorithm == "Minimax":
            ai.get_best_move_alphabeta(board, Connect4.AI_TURN, Connect4.PLAYER_TURN, Connect4.EMPTY,
                                       Connect4.POSITIVE_POSITION_SCORES, Connect4.NEGATIVE_POSITION_SCORES)

        elif algorithm == "Alpha-Beta":
            ai.get_best_move_alphabeta(board, Connect4.AI_TURN, Connect4.PLAYER_TURN, Connect4.EMPTY,
                                       Connect4.POSITIVE_POSITION_SCORES, Connect4.NEGATIVE_POSITION_SCORES)
        end_time = time.time()

        total_time += end_time - start_time

    average_time = total_time / 10  # Calculate the average execution time

    return average_time

def main():
    depth = 7 # Specify the depth for the algorithms

    minimax_average_time = measure_algorithm_performance("Minimax", depth)
    alpha_beta_average_time = measure_algorithm_performance("Alpha-Beta", depth)
    print("Average execution time for Minimax:", minimax_average_time)
    print("Average execution time for Alpha-Beta:", alpha_beta_average_time)
    algorithms = ["Minimax", "Alpha-Beta"]
    average_times = [minimax_average_time, alpha_beta_average_time]

    plt.bar(algorithms, average_times)
    plt.xlabel("Algorithm")
    plt.ylabel("Average Execution Time (s)")
    plt.title("Algorithm Performance Comparison")
    plt.show()

if __name__ == "__main__":
    main()