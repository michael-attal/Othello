from views.board_view import BoardView
from models.board import Board


class BoardConsoleView(BoardView):
    def __init__(self, board: Board):
        super().__init__(board)

    def draw_board(self):
        board_size = self.board.size + 1  # NOTE: Add one to the size to show row and col value in top of the board
        footer = "-" * (4 * board_size - 1)
        for i in range(board_size):
            for j in range(board_size):
                if i == 0 and j == 0:
                    print(f"  | ", end="")
                elif j == 0:
                    print(f"{(i)} ", end="")
                elif i == 0:
                    if j != board_size - 1:
                        print(f"{(j)} | ", end="")
                    else:
                        print(f"{(j)} ", end="")
                else:
                    cell = self.board.get_cell(i - 1, j - 1)  # NOTE: Remove one because the board console view ask to enter a row and col starting by 1
                    print(f"| {cell} ", end="")
            # if j != board_size - 1:
            print("|")
            print(footer)
