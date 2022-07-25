from models.color import Color
from models.position import Position


class Disk:
    def __init__(self, color: Color, position: Position):
        self.color = color
        self.position = position
