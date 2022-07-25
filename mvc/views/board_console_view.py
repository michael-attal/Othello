from views.board_view import BoardView
from models.board import Board


class BoardConsoleView(BoardView):
    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def draw_board(self):
        board_size = self.board.size
        header = "-" * (4 * board_size + 1)
        print(header)
        for i in range(board_size):
            for j in range(board_size):
                cell = self.board.get_cell(i, j)
                print(f"| {cell} ", end="")
            print("|")
            print(header)
