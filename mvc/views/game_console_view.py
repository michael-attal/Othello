from views.game_view import GameView
from views.board_console_view import BoardConsoleView
from models.game import Game
from models.player import Player


class GameConsoleView(GameView):
    def __init__(self, game: Game) -> None:
        super().__init__(game)
        self.board_view = BoardConsoleView(game.board)

    def get_move(self, curr_player: Player):
        print(f"{curr_player.name} it's your turn (You play {curr_player.symbol} symbol)")
        s = input("Enter your move (row, col):").split(",")
        row, col = int(s[0]), int(s[1])
        # NOTE: Becase board_console_view add one row and one col to show which case has which num we must minus by one the number getted from player.
        row -= 1
        col -= 1
        return row, col

    def draw_board(self):
        self.board_view.draw_board()

    def display_not_valid_move(self):
        print("Error! Please enter a correct move")

    def display_winner(self, player: Player):
        print(f"Congratualition {player.name}, you win!")
