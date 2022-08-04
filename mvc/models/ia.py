from models.player import Player


class IA(Player):
    def __init__(self, name, symbol, difficulty="medium"):
        super().__init__(name, symbol)
        self.difficulty = difficulty
