from models.games_rules import GamesRules
from models.board import Board
from models.player import Player


class ClassicRules(GamesRules):
    def __init__(self, board: Board, players: list[Player]):
        super().__init__(board, players)

    def is_valid_move(self, row, col, curr_player: Player):
        if row >= 0 and col >= 0:
            if row < self.board.size and col < self.board.size:
                curr_cell = self.board.get_cell(row, col)
                if curr_cell == " ":
                    if self.is_next_cells_valid(row, col, curr_player) == True:
                        return True
        return False

    def is_next_cells_valid(self, row, col, curr_player: Player, only_check_direction="", change_next_cells_to_curr_player=False):
        top_cell = " "
        top_left_cell = " "
        top_right_cell = " "
        left_cell = " "
        right_cell = " "
        bottom_cell = " "
        bottom_left_cell = " "
        bottom_right_cell = " "
        if row > 0:
            if only_check_direction == "" or only_check_direction == "top":
                top_cell = self.board.get_cell(row - 1, col)
            if col > 0:
                if only_check_direction == "" or only_check_direction == "top_left":
                    top_left_cell = self.board.get_cell(row - 1, col - 1)
            if col < self.board.size - 2:
                if only_check_direction == "" or only_check_direction == "top_right":
                    top_right_cell = self.board.get_cell(row - 1, col + 1)
        if col > 0:
            if only_check_direction == "" or only_check_direction == "left":
                left_cell = self.board.get_cell(row, col - 1)
        if col < self.board.size - 2:
            if only_check_direction == "" or only_check_direction == "right":
                right_cell = self.board.get_cell(row, col + 1)
                print(right_cell)
        if row < self.board.size - 2:
            if only_check_direction == "" or only_check_direction == "bottom":
                bottom_cell = self.board.get_cell(row + 1, col)
            if col > 0:
                if only_check_direction == "" or only_check_direction == "bottom_left":
                    bottom_left_cell = self.board.get_cell(row + 1, col - 1)
            if col < self.board.size - 2:
                if only_check_direction == "" or only_check_direction == "bottom_right":
                    bottom_right_cell = self.board.get_cell(row + 1, col + 1)

        if top_cell != " " and top_cell != curr_player.symbol:
            # NOTE: Now check that one of the next next top cell is owned from curr_player to allow the move
            if row > 0:
                is_next_next_curr_player = self.is_next_cells_valid(row - 1, col, curr_player, "top")
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if top_left_cell != " " and top_left_cell != curr_player.symbol:
            if row > 0 and col > 0:
                is_next_next_curr_player = self.is_next_cells_valid(row - 1, col - 1, curr_player, "top_left")
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if top_right_cell != " " and top_right_cell != curr_player.symbol:
            if row > 0 and col < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row - 1, col + 1, curr_player, "top_right")
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if left_cell != " " and left_cell != curr_player.symbol:
            if col > 0:
                is_next_next_curr_player = self.is_next_cells_valid(row, col - 1, curr_player, "left")
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if right_cell != " " and right_cell != curr_player.symbol:
            if col < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row, col + 1, curr_player, "right")
                print(is_next_next_curr_player)
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if bottom_cell != " " and bottom_cell != curr_player.symbol:
            # NOTE: Now check that one of the next next top cell if owned from curr_player to allow the move
            if row < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row + 1, col, curr_player, "bottom")
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if bottom_left_cell != " " and bottom_left_cell != curr_player.symbol:
            if row < self.board.size - 2 and col > 0:
                is_next_next_curr_player = self.is_next_cells_valid(row + 1, col - 1, curr_player, "bottom_left")
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if bottom_right_cell != " " and bottom_right_cell != curr_player.symbol:
            if row < self.board.size - 2 and col < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row + 1, col + 1, curr_player, "bottom_right")
                if is_next_next_curr_player == curr_player.symbol:
                    return True

        if (
            top_cell == curr_player.symbol
            or top_right_cell == curr_player.symbol
            or top_left_cell == curr_player.symbol
            or left_cell == curr_player.symbol
            or right_cell == curr_player.symbol
            or bottom_cell == curr_player.symbol
            or bottom_right_cell == curr_player.symbol
            or bottom_left_cell == curr_player.symbol
        ):
            return curr_player.symbol

        if top_cell == " " or top_right_cell == " " or top_left_cell == " " or left_cell == " " or right_cell == " " or bottom_cell == " " or bottom_right_cell == " " or bottom_left_cell == " ":
            return " "

        return False

    def get_valid_moves(self, board, disk):
        # TODO Get every moves possible from actual board (loop all entries from the board and check if is_valid_move return True, then add this moves to the list)
        pass

    def is_game_over(self, board):
        # TODO Check that no valid moves is possible from get_valid_moves and then return true
        return False

    def get_winner(self):
        # TODO Check board.mat value and return the player who have the most symbol in the matrice. If it's equal return None
        return self.players[0]
