import tkinter as tk
from copy import deepcopy
from Connect4 import Connect4
from Connect4AI import Connect4AI
from randomai import RandomAI

class Connect4GUI:
    def __init__(self, ai_depth, ai_mode):
        self.root = tk.Tk()
        self.root.title("Connect 4")
        self.board = Connect4()
        self.ai = Connect4AI(depth=ai_depth)
        self.random_ai = RandomAI()

        self.canvas = tk.Canvas(self.root, width=700, height=600, bg='blue')
        self.canvas.pack()

        self.root.bind("<Button-1>", self.handle_click)

        self.draw_board()

        self.root.mainloop()


    def draw_board(self):
        self.canvas.delete("all")
        for col in range(self.board.column_count):
            for row in range(self.board.row_count):
                x1 = col * 100
                y1 = row * 100
                x2 = x1 + 100
                y2 = y1 + 100
                self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill='white')
                if self.board.grid[row][col] == self.board.PLAYER_TURN:
                    self.canvas.create_oval(x1 + 15, y1 + 15, x2 - 15, y2 - 15, fill='red')
                elif self.board.grid[row][col] == self.board.AI_TURN:
                    self.canvas.create_oval(x1 + 15, y1 + 15, x2 - 15, y2 - 15, fill='yellow')
        self.root.update()

    def handle_click(self, event):
        if self.board.current_player == self.board.PLAYER_TURN:
            col = event.x // 100
            if self.board.is_valid_move(col):
                self.board.make_move(col)
                self.draw_board()
                if self.board.check_win():
                    self.display_game_result()
                elif not self.board.is_board_full():
                    self.make_ai_move()
                    if self.board.check_win():
                        self.display_game_result()
                else:
                    self.display_game_result()

    def make_ai_move(self):
        if ai_mode == 'alphabeta':
            col = self.ai.get_best_move_alphabeta(self.board, self.board.AI_TURN, self.board.PLAYER_TURN,
                                                  self.board.EMPTY, self.board.POSITIVE_POSITION_SCORES,
                                                  self.board.NEGATIVE_POSITION_SCORES)
        else:  # ai_mode == 'minimax'
            col = self.ai.get_best_move_minimax(self.board, self.board.AI_TURN, self.board.PLAYER_TURN,
                                                self.board.EMPTY, self.board.POSITIVE_POSITION_SCORES,
                                                self.board.NEGATIVE_POSITION_SCORES)
        self.board.make_move(col)
        self.draw_board()

    def display_game_result(self):
        if self.board.check_win():
            if self.board.current_player == self.board.PLAYER_TURN:
                result = "AI wins!"
            else:
                result = "Player wins!"
        else:
            result = "Game ends in a draw."

        label = tk.Label(self.root, text=result, font=("Arial", 24), bg='blue', fg='white')
        label.pack()


if __name__ == '__main__':
    ai_depth = int(input("Choose AI depth (an integer between 1 and 10): "))
    ai_mode = input("Choose AI mode ('alphabeta' or 'minimax'): ")

    Connect4GUI(ai_depth, ai_mode)
