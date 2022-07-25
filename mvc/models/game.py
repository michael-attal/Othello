from models.board import Board
from models.games_rules import GamesRules
from models.player import Player


class Game:
    def __init__(self, board: Board, rules: GamesRules, players: Player):
        self.board = board
        self.rules = rules
        self.players = players
        self.curr_player = players[0]

    def make_move(self, row, col, player: Player):
        self.board.update_cell(row, col, player)

    def check_winner(self):
        # TODO
        pass

    def change_player(self):
        if self.curr_player == self.players[0]:
            self.curr_player = self.players[1]
        else:
            self.curr_player = self.players[0]
