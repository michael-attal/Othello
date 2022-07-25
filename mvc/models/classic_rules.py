from models.games_rules import GamesRules
from models.board import Board
from models.player import Player


class ClassicRules(GamesRules):
    def __init__(self, board: Board, players: Player, current_player: Player):
        super().__init__(board, players, current_player)

    def is_valid_move(self, board, disk):
        return True

    def get_valid_moves(self, board, disk):
        pass

    def is_game_over(self, board):
        pass

    def get_winner(self, board):
        pass
