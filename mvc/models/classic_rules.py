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

    def is_next_cells_valid(self, row, col, current_player, only_check_direction="", change_next_cells_to_current_player=False):
        directions = {
            "top": (-1, 0),
            "top_left": (-1, -1),
            "top_right": (-1, 1),
            "left": (0, -1),
            "right": (0, 1),
            "bottom": (1, 0),
            "bottom_left": (1, -1),
            "bottom_right": (1, 1),
        }

        def is_valid_position(row_idx, col_idx):
            return 0 <= row_idx < self.board.size and 0 <= col_idx < self.board.size

        def check_direction(direction):
            row_delta, col_delta = directions[direction]
            next_row, next_col = row + row_delta, col + col_delta
            if not is_valid_position(next_row, next_col):
                return False
            cell = self.board.get_cell(next_row, next_col)
            if cell == " " or cell == current_player.symbol:
                return False

            while True:
                next_row, next_col = next_row + row_delta, next_col + col_delta
                if not is_valid_position(next_row, next_col):
                    return False
                cell = self.board.get_cell(next_row, next_col)
                if cell == " ":
                    return False
                if cell == current_player.symbol:
                    if change_next_cells_to_current_player:
                        while (next_row - row_delta, next_col - col_delta) != (row, col):
                            next_row, next_col = next_row - row_delta, next_col - col_delta
                            self.board.update_cell(next_row, next_col, current_player)
                        self.board.update_cell(row, col, current_player)
                    return True

        if only_check_direction:
            return check_direction(only_check_direction)
        else:
            for direction in directions:
                if check_direction(direction):
                    return True

        return False

    def get_valid_moves(self, curr_player: Player) -> list:
        # NOTE: Get every moves possible from actual board for a player
        moveAvalaibles = []
        for row in range(self.board.size):
            for col in range(self.board.size):
                if self.is_valid_move(row, col, curr_player):
                    moveAvalaibles.append((row, col))
        return moveAvalaibles

    def make_move(self, row, col, curr_player: Player):
        # NOTE: Update all cells between the new one and the old one from board
        self.is_next_cells_valid(row, col, curr_player, "", True)

    def is_game_over(self):
        # NOTE: Check that no valid moves is possible for any players
        for player in self.players:
            if len(self.get_valid_moves(player)) > 0:
                return False
        return True

    def get_count_symbols_of_players(self):
        count_symbols_player_one = 0
        count_symbols_player_two = 0
        for row in range(self.board.size):
            for col in range(self.board.size):
                if self.board.get_cell(row, col) == self.players[0].symbol:
                    count_symbols_player_one += 1
                elif self.board.get_cell(row, col) == self.players[1].symbol:
                    count_symbols_player_two += 1

        return {self.players[0].symbol: count_symbols_player_one, self.players[1].symbol: count_symbols_player_two}

    def get_winner(self):
        # NOTE: Return the player who have the most symbol in the matrice. If it's equal return None
        symbol_player_one = self.players[0].symbol
        symbol_player_two = self.players[1].symbol
        count_symbols = self.get_count_symbols_of_players()
        if count_symbols[symbol_player_one] > count_symbols[symbol_player_two]:
            return self.players[0]
        elif count_symbols[symbol_player_two] > count_symbols[symbol_player_one]:
            return self.players[1]
        else:
            return None
