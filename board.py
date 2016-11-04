import config


class Board:
    def __init__(self):
        board = [[config.EMPTY for x in range(config.BOARD_SIZE)] for y in
                 range(config.BOARD_SIZE)]
        self.board = board

    def print_heading(self):
        print("   " + " ".join([chr(c) for c in range(ord('A'), ord('A') +
                                                      config.BOARD_SIZE)]))

    def print_board(self):
        self.print_heading()

        row_number = 1
        for row in self.board:
            print(str(row_number).rjust(2) + ' ' + (' '.join(row)))
            row_number += 1
