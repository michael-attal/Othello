from abc import ABC, abstractclassmethod


class Player(ABC):
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
