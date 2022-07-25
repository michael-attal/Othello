from abc import ABC, abstractmethod


class GameView(ABC):
    def __init__(self, gameModel) -> None:
        self.game = gameModel

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def display_not_valid_move(self):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass
