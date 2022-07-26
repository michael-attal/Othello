from abc import ABC, abstractclassmethod

from models.board import Board
from models.player import Player


class GamesRules(ABC):
    def __init__(self, board: Board, players: list[Player]):
        self.board = board
        self.players = players

    @abstractclassmethod
    def is_valid_move(self, row, col, curr_player: Player):
        pass

    @abstractclassmethod
    def get_valid_moves(self, curr_player: Player):
        pass

    @abstractclassmethod
    def make_move(self, row, col, curr_player: Player):
        pass

    @abstractclassmethod
    def is_game_over(self):
        pass

    @abstractclassmethod
    def get_winner(self):
        pass
