from views.game_view import GameView
from models.game import Game


class GameController:
    def __init__(self, gameModel: Game, gameView: GameView):
        self.model = gameModel
        self.view = gameView

    def run_game(self):
        while True:
            self.view.draw_board()

            row, col = self.view.get_move(self.model.curr_player)
            while not self.model.rules.is_valid_move(row, col):
                # TODO display error message in the view
                print("Error! Please enter a correct move")
                row, col = self.view.get_move()

            self.model.make_move(row, col, self.model.curr_player)
            player = self.model.check_winner()
            if player:
                self.view.display_winner(player)
                break

            self.model.change_player()
