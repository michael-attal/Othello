from abc import ABC, abstractclassmethod

from models.board import Board
from models.player import Player


class GamesRules(ABC):
    def __init__(self, board: Board, players: list[Player]):
        self.board = board
        self.players = players

    @abstractclassmethod
    def is_valid_move(self, row, col):
        pass

    @abstractclassmethod
    def get_valid_moves(self, board, disk):
        pass

    @abstractclassmethod
    def is_game_over(self, board):
        pass

    @abstractclassmethod
    def get_winner(self, board):
        pass
