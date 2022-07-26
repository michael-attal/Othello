# from models.disk import Disk
# from models.color import Color
# from models.position import Position
from models.player import Player


class Board:
    def __init__(self, size: int, players: list[Player], number_of_disk_to_start=4):
        self.size = size
        self.mat = [[" "] * size for _ in range(size)]
        self.players = players
        self.number_of_disk_to_start = number_of_disk_to_start

        middle = (size - 1) // 2
        print(self.mat[middle][middle])
        self.mat[middle][middle] = players[1].symbol
        self.mat[middle][middle + 1] = players[0].symbol
        self.mat[middle + 1][middle] = players[0].symbol
        self.mat[middle + 1][middle + 1] = players[1].symbol
        # self.disks = []
        # for i in range(len(players)):
        #     for j in range(number_of_disk_to_start):
        #         if j % 2 == 0:
        #             self.disks.append(Disk(Color("X"), Position(size // 2, size // 2)))  # FIXME: Add position from middle of the board and alternate player
        #         else:
        #             self.disks.append(Disk(Color("O"), Position(size // 2 + 1, size // 2 + 1)))  # FIXME: Add different symbol if more then 2 players

    def get_cell(self, row, col):
        # TODO Compare that row < board.size and same for col
        return self.mat[row][col]

    def update_cell(self, row, col, player: Player):
        self.mat[row][col] = player.symbol
