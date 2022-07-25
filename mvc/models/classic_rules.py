from models.games_rules import GamesRules
from models.board import Board
from models.player import Player


class ClassicRules(GamesRules):
    def __init__(self, board: Board, players: Player, current_player: Player):
        super().__init__(board, players, current_player)

    def is_valid_move(self, row, col):
        if row >= 0 and col >= 0:
            if row < self.board.size and col < self.board.size:
                if self.board.get_cell(row, col) == " ":
                    # TODO Now check if diagonal / horizontal / vertical contain at least one symbol of opponent.
                    return True
        return False

    def get_valid_moves(self, board, disk):
        # TODO Get every moves possible from actual board
        pass

    def is_game_over(self, board):
        # TODO Check that no valid moves is possible
        return False

    def get_winner(self):
        # TODO Check board.mat value and return the player who have the most symbol in the matrice. If it's equal return None
        return self.current_player
