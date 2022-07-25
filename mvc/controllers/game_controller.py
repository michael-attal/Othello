from views.game_view import GameView
from models.game import Game


class GameController:
    def __init__(self, gameModel: Game, gameView: GameView):
        self.model = gameModel
        self.view = gameView

    def run_game(self):
        while not self.model.rules.is_game_over(self.model.board):
            self.view.draw_board()

            row, col = self.view.get_move(self.model.curr_player)
            while not self.model.rules.is_valid_move(row, col):
                self.view.display_not_valid_move(player)
                row, col = self.view.get_move(self.model.curr_player)

            self.model.make_move(row, col, self.model.curr_player)
            self.model.change_player()

        player = self.model.rules.get_winner()
        if player:
            self.view.display_winner(player)
