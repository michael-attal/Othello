from models.player import Player


class HumanPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
