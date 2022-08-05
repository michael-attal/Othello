from models.ai import AI
from views.game_view import GameView
from views.board_console_view import BoardConsoleView
from models.game import Game
from models.player import Player


class GameConsoleView(GameView):
    def __init__(self, game: Game = None) -> None:
        super().__init__(game)
        self.board_view = None
        if game != None:
            self.board_view = BoardConsoleView(game.board)

    def get_game_option(self):
        player_choice = input("Your choice: ")
        return player_choice

    def get_player_name(self, player_number, symbol_player):
        print(f"Player {player_number}, please enter your name (you will play symbol {symbol_player})")
        player_name = input("Your name: ")
        return player_name

    def get_ai_difficulty(self):
        ai_difficulty = input("Your choice: ")
        return ai_difficulty

    def display_welcome_message(self):
        print("Hello and welcome to the Reversi (Also called Othello) game!")

    def display_lets_start_the_game_message(self):
        print("Great, let's start the game!")

    def display_goodbye_message(self):
        print("Hope to see you soon, bye!")

    def display_game_options(self):
        print("Please select an option between 1,2 or 0")
        print('"1" Player VS AI')
        print('"2" Player VS Player')
        print('"0" Quit the game')

    def display_ai_informations_message(self):
        print("You will play against the AI called Terminator. Be strong!")

    def display_available_ai_difficulties(self):
        print("Please enter the difficulty of the AI:")
        print('"1" for Easy')
        print('"2" for Medium')
        print('"3" for Hard')
        print('"4" for Very hard')

    def get_move(self, curr_player: Player):
        print(f"{curr_player.name} it's your turn (You play {curr_player.symbol} symbol)")
        s = input("Enter your move (row, col):").split(",")
        row, col = int(s[0]), int(s[1])
        # NOTE: Because board_console_view add one row and one col to show which cell has which num we must minus by one the number getted from player.
        row -= 1
        col -= 1
        return row, col

    def draw_board(self):
        self.board_view.draw_board()

    def display_invalid_game_option_selected(self):
        print("Please enter a correct option!")

    def display_invalid_game_option_selected(self):
        print("Please enter a correct AI difficulty option!")

    def display_not_valid_move(self):
        print("Error! Please enter a correct move")

    def display_ia_move(self, row, col):
        print(f"AI played row: {(row) +1} and col: {(col)+1}.")  # NOTE: Don't forget to add +1 to show correct formatted row and col selected by AI

    def display_winner(self, player: Player):
        if isinstance(player, AI):
            print(f"The AI {player.name}, win. Soon, this AI will conquer the world!")
        else:
            print(f"Congratualition {player.name}, you win!")

    def display_no_winner(self, player: Player):
        print("There is no winner, it's a perfect tie!")
