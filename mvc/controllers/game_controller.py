from views.game_console_view import GameConsoleView
from views.game_view import GameView
from models.game import Game
from models.ia import IA


class GameController:
    def __init__(self, gameModel: Game, gameView: GameView):
        self.model = gameModel
        self.view = gameView

    def run_game(self):
        while not self.model.rules.is_game_over():
            # NOTE: If no valid move is availables for the current players, just change to the next player
            if len(self.model.rules.get_valid_moves(self.model.curr_player)) > 0:
                self.view.draw_board()
                if isinstance(self.model.curr_player, IA):
                    # move = self.model.rules.get_highest_scored_move_for_ia(self.model.curr_player)
                    move = self.model.rules.get_move_for_ia(self.model.curr_player)
                    row = move[0]
                    col = move[1]
                    if isinstance(self.view, GameConsoleView):  # NOTE: Show a print line with the move selected by IA for better ux experience.
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
