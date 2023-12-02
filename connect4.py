import logging
from constants import (
    INVALID_INPUT_MESSAGE,
    INVALID_COLUMN_MESSAGE,
    WIN_MESSAGE,
    DRAW_MESSAGE,
    COLUMN_FULL_MESSAGE,
    MOVE_PROMPT
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ConnectFour")


class ConnectFour:
    def __init__(self, rows=6, cols=7) -> None:
        self.rows = rows
        self.cols = cols
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'

    def execute(self) -> None:
        self.display_board()

        while True:
            col = self.get_valid_column_input()
            if self.make_and_display_move(col):
                break

    def make_and_display_move(self, col) -> bool:
        if self.make_move(col):
            self.display_board()
            if self.check_winner():
                logger.info(WIN_MESSAGE.format(player=self.current_player))
                return True
            if all(cell != ' ' for row in self.board for cell in row):
                logger.info(DRAW_MESSAGE)
                return True
            self.switch_player()
        else:
            logger.warning(COLUMN_FULL_MESSAGE)
        return False

    def get_valid_column_input(self) -> int:
        while True:
            try:
                col = int(input(MOVE_PROMPT.format(player=self.current_player)))
                if 0 <= col < self.cols:
                    return col
                else:
                    logger.warning(INVALID_COLUMN_MESSAGE.format(max_col=self.cols))
            except ValueError:
                logger.warning(INVALID_INPUT_MESSAGE)

    def display_board(self) -> None:
        for row in self.board:
            print('|'.join(row))
        print('-' * (self.cols * 2 - 1))
        print(' '.join(str(i) for i in range(self.cols)))

    def make_move(self, col) -> bool:
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                return True
        return False

    def switch_player(self) -> None:
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_horizontal_winner(self) -> bool:
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if self.check_consecutive_cells(row, col, 0, 1):
                    return True
        return False

    def check_vertical_winner(self) -> bool:
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if self.check_consecutive_cells(row, col, 1, 0):
                    return True
        return False

    def check_diagonal_winner(self) -> bool:
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if self.check_consecutive_cells(row, col, 1, 1):
                    return True
                if self.check_consecutive_cells(row, col + 3, 1, -1):
                    return True
        return False

    def check_winner(self) -> bool:
        return self.check_horizontal_winner() or self.check_vertical_winner() or self.check_diagonal_winner()

    def check_consecutive_cells(self, start_row, start_col, row_step, col_step) -> bool:
        if row_step == 0 and col_step == 0:
            return False
        player = self.board[start_row][start_col]
        return (
            player != ' ' and
            all(self.board[row][col] == player for row, col in
                zip(range(start_row, start_row + 4 * row_step, row_step) if row_step != 0 else [start_row] * 4,
                    range(start_col, start_col + 4 * col_step, col_step) if col_step != 0 else [start_col] * 4))
        )
