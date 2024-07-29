class Connect4:
    AI_TURN = 'X'
    PLAYER_TURN = 'O'
    EMPTY = '.'
    POSITIVE_POSITION_SCORES = [1, 10, 100, 1000]
    NEGATIVE_POSITION_SCORES = [1, 10, 100, 1000]

    def __init__(self, row_count=6, column_count=7, window_length=4):
        self.row_count = row_count
        self.column_count = column_count
        self.window_length = window_length
        self.current_player = self.PLAYER_TURN
        self.grid = [[self.EMPTY] * self.column_count for _ in range(self.row_count)]

    def make_move(self, column):
        if not self.is_valid_move(column):
            raise ValueError("Invalid move")

        for row in range(self.row_count - 1, -1, -1):
            if self.grid[row][column] == self.EMPTY:
                self.grid[row][column] = self.current_player
                break

        self.current_player = self.AI_TURN if self.current_player == self.PLAYER_TURN else self.PLAYER_TURN

    def is_valid_move(self, column):
        return 0 <= column < self.column_count and self.grid[0][column] == self.EMPTY

    def get_valid_moves(self):
        valid_moves = []
        for col in range(self.column_count):
            if self.is_valid_move(col):
                valid_moves.append(col)
        return valid_moves

    def check_win(self):
        return self.check_rows() or self.check_columns() or self.check_diagonals()

    def check_rows(self):
        for row in range(self.row_count):
            for col in range(self.column_count - self.window_length + 1):
                window = self.grid[row][col:col+self.window_length]
                if self.check_window(window):
                    return True
        return False

    def check_columns(self):
        for col in range(self.column_count):
            for row in range(self.row_count - self.window_length + 1):
                window = [self.grid[row+i][col] for i in range(self.window_length)]
                if self.check_window(window):
                    return True
        return False

    def check_diagonals(self):
        for row in range(self.row_count - self.window_length + 1):
            for col in range(self.column_count - self.window_length + 1):
                window = [self.grid[row+i][col+i] for i in range(self.window_length)]
                if self.check_window(window):
                    return True

        for row in range(self.row_count - 1, self.window_length - 2, -1):
            for col in range(self.column_count - self.window_length + 1):
                window = [self.grid[row-i][col+i] for i in range(self.window_length)]
                if self.check_window(window):
                    return True

        return False

    def check_window(self, window):
        return (
            window.count(self.PLAYER_TURN) == self.window_length or
            window.count(self.AI_TURN) == self.window_length
        )

    def is_board_full(self):
        for col in range(self.column_count):
            if self.grid[0][col] == self.EMPTY:
                return False
        return True

    def print_board(self):
        for row in self.grid:
            print(' '.join(row))
        print()
