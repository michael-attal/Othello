from abc import ABC, abstractmethod
from models.board import Board


class BoardView(ABC):
    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def draw_board(self):
        pass
