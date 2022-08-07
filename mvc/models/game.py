from datetime import datetime

from models.board import Board
from models.games_rules import GamesRules
from models.player import Player


class Game:
    def __init__(self, board: Board, rules: GamesRules, players: list[Player]):
        self.board = board
        self.rules = rules
        self.players = players
        self.curr_player = players[0]

    def change_player(self):
        if self.curr_player == self.players[0]:
            self.curr_player = self.players[1]
        else:
            self.curr_player = self.players[0]

    def save_game_result(self, players, winner: Player, score_players):
        now = datetime.now()
        file_name = f"othello_game_result_{now}"

        date_text = f"Date game: {now.month}/{now.day}/{now.year} at {now.hour}:{now.minute}.\n"
        winner_text = "There is no winner, it's a draw.\n"
        if winner != None:
            winner_text = f'The winner is {winner.name}, he played symbol "{winner.symbol}".\n'
        symbol_player_one = self.players[0].symbol
        symbol_player_two = self.players[1].symbol
        score_text = f'The symbol "{symbol_player_one}" has {score_players[symbol_player_one]} disks\n'
        score_text += f'The symbol "{symbol_player_two}" has {score_players[symbol_player_two]} disks\n'

        try:
            with open(file_name, "w") as dest_file:
                dest_file.write(date_text)
                dest_file.write(winner_text)
                dest_file.write(score_text)
        except PermissionError:
            print("Error permission: Can't read or write file.")
        except:
            print("An error occurs during the proccess.")
