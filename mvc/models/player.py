from abc import ABC, abstractclassmethod
from copy import deepcopy

from numpy import Infinity


class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # NOTE: Get a move is used to get a move for the AI but also for a futur implementation of a get hint method for a player. That's why the minimax implementation is done here
    # TODO: Implement a get hint choice (ex: when user is asked to enter row and col, if he enter hint, suggest a move)
    def get_a_move(self, rules, move_level=2) -> tuple:
        """Get a move for the AI or the player if he ask for a hint move.

        Args:
            rules (GamesRules): The current game rules (needed, because some custom rules can be applied when checking a move, make a move...)
            move_level (int, optional): The difficulty of the move. A larger number means more depth in the minimax function and a better heuristic function applied. Defaults to 2. Should not exceed 6 or it will take too much time to process.

        Returns:
            tuple: The calculated best move to do
        """

        backup_mat = deepcopy(rules.board.mat)
        best_move_value = float(-Infinity)
        best_row = 0
        best_col = 0
        # TODO Apply a heuristic function depending of the move level selected
        depth = move_level

        move_availables = rules.get_valid_moves(self)  # NOTE: Get all valid moves depending of the board and the rules applied

        for move_available in move_availables:
            row = move_available[0]
            col = move_available[1]
            backup_mat = deepcopy(rules.board.mat)
            rules.make_move(row, col, self)
            score_current_move = self.minimax(rules, self, True, depth)
            rules.board.mat = deepcopy(backup_mat)
            if score_current_move >= best_move_value:
                best_move_value = score_current_move
                best_row = row
                best_col = col

        return best_row, best_col

    def minimax(self, rules, curr_player: "Player", is_maximizing: bool, depth: int = 2):
        """Get the best move to play for the current player from the board. Its must often used for AI, but can also be used if we want to implement a "hint" function. Atm it's only used by AI.

        Args:
            rules (Player): The current game rules (needed, because some custom rules can be applied when checking a move, make a move...)
            curr_player (Player): The current player to evaluate
            depth (int): The depth to get the minimax value (should not exceed 4 or it take too much time)
            is_maximizing (bool): Used to know if we are trying to get the highest value or the lowest (minimizing)

        Returns:
            int: A number that evaluted the board.
        """

        is_game_over = rules.is_game_over()
        if depth == 0 or is_game_over:
            if is_game_over:
                winner = rules.get_winner()
                if curr_player == winner:
                    return 1
                elif winner == None:
                    return 0
                else:
                    return -1
            else:
                # NOTE: We are on the lowest depth, stop computation just return if curr player has more symbols (1), less (-1) or equal (0)
                # NOTE: Later use heurestic function to calculate also if the actual player has some corners (0,0 | 0,size-1 | size-1,0 | size-1,size-1) which is a very good position and add score to the evaluated value
                symbol_curr_player = curr_player.symbol
                symbol_player_two = rules.players[0].symbol
                if symbol_player_two == symbol_curr_player:
                    symbol_player_two = rules.players[1].symbol

                count_symbols = rules.get_count_symbols_of_players()

                if count_symbols[symbol_curr_player] > count_symbols[symbol_player_two]:
                    return 1
                elif count_symbols[symbol_player_two] > count_symbols[symbol_curr_player]:
                    return -1
                else:
                    return 0

        if is_maximizing:
            max_evaluate_value = float(-Infinity)
            # NOTE: We make the move, and for each move we get the best value from them.
            move_availables = rules.get_valid_moves(curr_player)

            for move_available in move_availables:
                opponent = rules.players[0]
                if opponent == curr_player:
                    opponent = rules.players[1]
                row = move_available[0]
                col = move_available[1]
                backup_mat = deepcopy(rules.board.mat)
                rules.make_move(row, col, curr_player)
                evaluated_opponent_move = self.minimax(rules, opponent, False, depth - 1)
                max_evaluate_value = max(max_evaluate_value, evaluated_opponent_move)
                rules.board.mat = deepcopy(backup_mat)  # NOTE: Get back to the previous board
            return max_evaluate_value

        else:
            min_evaluate_value = float(Infinity)
            move_availables = rules.get_valid_moves(curr_player)

            for move_available in move_availables:
                opponent = rules.players[0]
                if opponent == curr_player:
                    opponent = rules.players[1]
                row = move_available[0]
                col = move_available[1]
                backup_mat = deepcopy(rules.board.mat)
                rules.make_move(row, col, curr_player)
                evaluated_opponent_move = self.minimax(rules, opponent, True, depth - 1)
                min_evaluate_value = min(min_evaluate_value, evaluated_opponent_move)
                rules.board.mat = deepcopy(backup_mat)
            return min_evaluate_value

    def heuristic_othello(self):
        pass
