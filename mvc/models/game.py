from models.board import Board
from models.games_rules import GamesRules
from models.player import Player


class Game:
    def __init__(self, board: Board, rules: GamesRules, players: list[Player]):
        self.board = board
        self.rules = rules
        self.players = players
        self.curr_player = players[0]

    def change_player(self):
        if self.curr_player == self.players[0]:
            self.curr_player = self.players[1]
        else:
            self.curr_player = self.players[0]
