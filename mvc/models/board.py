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
        # self.mat[3][1] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][2] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][4] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][5] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][6] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE

        # self.mat[1][1] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[1][2] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[1][3] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[1][4] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[2][1] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[2][2] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[2][3] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[2][4] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][1] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][2] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][3] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[3][4] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[4][1] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[4][2] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[4][3] = players[1].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE
        # self.mat[4][4] = players[0].symbol  # FIXME: TO REMOVE HERE FOR TESTING PURPOSE

    def get_cell(self, row, col):
        return self.mat[row][col]

    def update_cell(self, row, col, player: Player):
        self.mat[row][col] = player.symbol
