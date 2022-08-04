from copy import deepcopy

from numpy import Infinity
from models.games_rules import GamesRules
from models.board import Board
from models.player import Player
from models.ia import IA


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
                is_next_next_curr_player = self.is_next_cells_valid(row - 1, col, curr_player, "top", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row - 1, col, curr_player)  # NOTE: To update the last cell
                    return True

        if top_left_cell != " " and top_left_cell != curr_player.symbol:
            if row > 0 and col > 0:
                is_next_next_curr_player = self.is_next_cells_valid(row - 1, col - 1, curr_player, "top_left", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row - 1, col - 1, curr_player)
                    return True

        if top_right_cell != " " and top_right_cell != curr_player.symbol:
            if row > 0 and col < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row - 1, col + 1, curr_player, "top_right", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row - 1, col + 1, curr_player)
                    return True

        if left_cell != " " and left_cell != curr_player.symbol:
            if col > 0:
                is_next_next_curr_player = self.is_next_cells_valid(row, col - 1, curr_player, "left", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row, col - 1, curr_player)
                    return True

        if right_cell != " " and right_cell != curr_player.symbol:
            if col < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row, col + 1, curr_player, "right", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row, col + 1, curr_player)
                    return True

        if bottom_cell != " " and bottom_cell != curr_player.symbol:
            if row < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row + 1, col, curr_player, "bottom", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row + 1, col, curr_player)
                    return True

        if bottom_left_cell != " " and bottom_left_cell != curr_player.symbol:
            if row < self.board.size - 2 and col > 0:
                is_next_next_curr_player = self.is_next_cells_valid(row + 1, col - 1, curr_player, "bottom_left", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row + 1, col - 1, curr_player)
                    return True

        if bottom_right_cell != " " and bottom_right_cell != curr_player.symbol:
            if row < self.board.size - 2 and col < self.board.size - 2:
                is_next_next_curr_player = self.is_next_cells_valid(row + 1, col + 1, curr_player, "bottom_right", change_next_cells_to_curr_player)
                if is_next_next_curr_player == curr_player.symbol or is_next_next_curr_player == True:
                    if change_next_cells_to_curr_player:
                        self.board.update_cell(row, col, curr_player)
                        self.board.update_cell(row + 1, col + 1, curr_player)
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

    def get_valid_moves(self, curr_player: Player) -> list:
        # NOTE: Get every moves possible from actual board for a player
        moveAvalaibles = []
        for row in range(self.board.size):
            for col in range(self.board.size):
                if self.is_valid_move(row, col, curr_player):
                    moveAvalaibles.append((row, col))
        return moveAvalaibles

    def get_highest_scored_move_for_ia(self, ia: IA):
        move_availables = self.get_valid_moves(ia)
        backup_mat = deepcopy(self.board.mat)
        moves_with_count_symbols_available_for_ia = {}

        for move_available in move_availables:
            row = move_available[0]
            col = move_available[1]
            self.make_move(row, col, ia)
            count_symbols_ia = 0
            for i in range(self.board.size):
                for j in range(self.board.size):
                    if self.board.get_cell(i, j) == ia.symbol:
                        count_symbols_ia += 1
            dict_index_formatted = f"{str(row)},{str(col)}"
            moves_with_count_symbols_available_for_ia[dict_index_formatted] = count_symbols_ia
            self.board.mat = deepcopy(backup_mat)

        move_to_make = ""
        highest_count_symbols = 0
        for move, count_symbols in moves_with_count_symbols_available_for_ia.items():
            if count_symbols > highest_count_symbols:
                highest_count_symbols = count_symbols
                move_to_make = move

        move_to_make = move_to_make.split(",")
        move_to_make[0] = int(move_to_make[0])
        move_to_make[1] = int(move_to_make[1])
        return move_to_make

    def get_move_for_ia(self, ia: IA):
        # Todo change depth depending on ia diffuclty
        backup_mat = deepcopy(self.board.mat)
        best_move_value = float(-Infinity)
        best_row = 0
        best_col = 0
        depth = 2
        if ia.difficulty == "very_hard":
            depth = 4
        elif ia.difficulty == "hard":
            depth = 3
        elif ia.difficulty == "medium":
            depth = 2
        elif ia.difficulty == "easy":
            depth = 1

        move_availables = self.get_valid_moves(ia)

        for move_available in move_availables:
            row = move_available[0]
            col = move_available[1]
            backup_mat = deepcopy(self.board.mat)
            self.make_move(row, col, ia)
            score_current_move = self.minimax(ia, True, depth)
            self.board.mat = deepcopy(backup_mat)
            if score_current_move >= best_move_value:
                best_move_value = score_current_move
                best_row = row
                best_col = col

        print("best_move_value:", best_move_value)
        print("best_row:", best_row)
        print("best_col:", best_col)
        return best_row, best_col

    def minimax(self, curr_player: Player, is_maximizing: bool, depth: int = 2):
        """Get the best move to play for the current player from the board. Its must often used for IA, but can also be used if we want to implement a "hint" function. Atm it's only used by IA.

        Args:
            curr_player (Player): The current player to evaluate
            depth (int): The depth to get the minimax value (should not exceed 4 or it take to much time)
            is_maximizing (bool): Used to know if we are trying to get the highest value or the lowest (minimizing)

        Returns:
            int: A number that evaluted the board.
        """

        is_game_over = self.is_game_over()
        if depth == 0 or is_game_over:
            if is_game_over:
                winner = self.get_winner()
                if curr_player == winner:
                    return 1
                elif winner == None:
                    return 0
                else:
                    return -1
            else:
                # We are on the lowest depth, stop computation just return if curr player has more symbols (1), less (-1) or equal (0)
                # Later use heurestic function to calculate also if the actual player has some corners (0,0 | 0,size-1 | size-1,0 | size-1,size-1) which is a very good position and add score to the evaluated value
                symbol_curr_player = curr_player.symbol
                symbol_player_two = self.players[0].symbol
                if symbol_player_two == symbol_curr_player:
                    symbol_player_two = self.players[1].symbol

                count_symbols = self.get_count_symbols_of_players()
                if count_symbols[symbol_curr_player] > count_symbols[symbol_player_two]:
                    return 1
                elif count_symbols[symbol_player_two] > count_symbols[symbol_curr_player]:
                    return -1
                else:
                    return 0

        if is_maximizing:
            max_evaluate_value = float(-Infinity)
            # We make the move, and for each move we get the best value from them.
            move_availables = self.get_valid_moves(curr_player)

            for move_available in move_availables:
                opponent = self.players[0]
                if opponent == curr_player:
                    opponent = self.players[1]
                row = move_available[0]
                col = move_available[1]
                backup_mat = deepcopy(self.board.mat)
                self.make_move(row, col, curr_player)
                evaluated_opponent_move = self.minimax(opponent, False, depth - 1)
                max_evaluate_value = max(max_evaluate_value, evaluated_opponent_move)
                self.board.mat = deepcopy(backup_mat)  # Get back to the original board
            return max_evaluate_value

        else:
            min_evaluate_value = float(Infinity)
            move_availables = self.get_valid_moves(curr_player)

            for move_available in move_availables:
                opponent = self.players[0]
                if opponent == curr_player:
                    opponent = self.players[1]
                row = move_available[0]
                col = move_available[1]
                backup_mat = deepcopy(self.board.mat)
                self.make_move(row, col, curr_player)
                evaluated_opponent_move = self.minimax(opponent, True, depth - 1)
                min_evaluate_value = min(min_evaluate_value, evaluated_opponent_move)
                self.board.mat = deepcopy(backup_mat)  # Get back to the original board
            return min_evaluate_value

    def heuristic_othello(self):
        pass

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
