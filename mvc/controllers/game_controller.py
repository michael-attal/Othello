from models.board import Board
from models.classic_rules import ClassicRules
from models.human_player import HumanPlayer
from models.game import Game
from models.ai import AI
from views.board_console_view import BoardConsoleView
from views.game_console_view import GameConsoleView
from views.game_view import GameView


class GameController:
    def __init__(self, interface="console", gameModel: Game = None, gameView: GameView = None):
        self.model = gameModel
        self.view = gameView
        self.interface = interface

    def init_game(self):
        if self.interface == "console":
            GameView = GameConsoleView()
            self.view = GameView

            self.view.display_welcome_message()
            self.view.display_game_options()
            player_choice = self.view.get_game_option()

            players = []

            while player_choice != "1" and player_choice != "2" and player_choice != "0":
                self.view.display_invalid_game_option_selected()
                self.view.display_game_options()
                player_choice = self.view.get_game_option()
                # TODO: Change game option by get_game_opponent and player_choice by opponent, and finaly change below condition to if opponent == "AI" ...

            first_player_name = self.view.get_player_name("one", "X")
            players.append(HumanPlayer(first_player_name, "X"))

            # NOTE: User has selected to quit the game
            if player_choice == "0":
                self.view.display_goodbye_message()
                return "exit"
            else:
                # NOTE: If user selected to play against the AI
                if player_choice == "1":
                    self.view.display_ai_informations_message()
                    self.view.display_available_ai_difficulties()
                    ai_difficulty_choice = self.view.get_ai_difficulty()

                    while ai_difficulty_choice not in ["1", "2", "3", "4"]:
                        self.view.display_invalid_ai_difficulty_selected()
                        self.view.display_available_ai_difficulties()
                        ai_difficulty_choice = self.view.get_ai_difficulty()

                    players.append(AI("Terminator", "O", AI.get_ai_difficulty_name_from_choice(ai_difficulty_choice)))
                # NOTE: If user selected to play against another player
                if player_choice == "2":
                    second_player_name = self.view.get_player_name("two", "O")
                    players.append(HumanPlayer(second_player_name, "O"))

                self.view.display_lets_start_the_game_message()

                board = Board(players)
                rules = ClassicRules(board, players)
                gameModel = Game(board, rules, players)
                self.view.board_view = BoardConsoleView(board)  # NOTE: Don't forget to add the board to the view after the initialization is complete.
                self.model = gameModel

                return player_choice
        elif self.interface == "gui":
            pass
        return "error"

    def run_game(self):
        while not self.model.rules.is_game_over():
            # NOTE: If no valid move is availables for the current players, just change to the next player
            if len(self.model.rules.get_valid_moves(self.model.curr_player)) > 0:
                self.view.draw_board()
                if isinstance(self.model.curr_player, AI):
                    # move = self.model.curr_player.get_highest_scored_move(self.model.rules) # NOTE: Not used anymore, since the easy mode (one depth and no heuristic function) of minimax is doing the same has this method - Just let it here because it was a requirement of the part 3 of this project (before implementing minimax algorithm).
                    move = self.model.curr_player.get_move(self.model.rules)
                    row = move[0]
                    col = move[1]
                    if self.interface == "console":  # NOTE: Show a print line with the move selected by AI for better ux experience.
                        self.view.display_ia_move(row, col)
                else:
                    row, col = self.view.get_move(self.model.curr_player)

                    while not self.model.rules.is_valid_move(row, col, self.model.curr_player):
                        self.view.display_not_valid_move()
                        row, col = self.view.get_move(self.model.curr_player)

                self.model.rules.make_move(row, col, self.model.curr_player)

            self.model.change_player()

        # NOTE Draw the final board before showing winner
        self.view.draw_board()
        player = self.model.rules.get_winner()
        if player:
            self.view.display_winner(player)
        else:
            self.view.display_no_winner()
