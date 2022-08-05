from models.player import Player
from models.games_rules import GamesRules


class HumanPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)

    def get_hint_move(self, rules: GamesRules):
        return super().get_a_move(rules, 4)  # TODO Ask to the user the strongness of the hint he want
