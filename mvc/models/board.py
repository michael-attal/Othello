from models.player import Player


class Board:
    def __init__(self, size: int, players: list[Player], number_of_disk_to_start=4):
        self.size = size
        self.mat = [[" "] * size for _ in range(size)]
        self.players = players
        self.number_of_disk_to_start = number_of_disk_to_start

        middle = (size - 1) // 2
        self.mat[middle][middle] = players[1].symbol
        self.mat[middle][middle + 1] = players[0].symbol
        self.mat[middle + 1][middle] = players[0].symbol
        self.mat[middle + 1][middle + 1] = players[1].symbol

    def get_cell(self, row, col):
        return self.mat[row][col]

    def update_cell(self, row, col, player: Player):
        self.mat[row][col] = player.symbol
