from models.board import Board
from models.classic_rules import ClassicRules
from models.human_player import HumanPlayer
from models.game import Game
from models.ai import AI

from views.board_gui_view import BoardGuiView
from views.game_gui_view import GameGuiView
from views.game_view import GameView


class GameGuiController:
    def __init__(self, gameModel: Game = None, gameView: GameView = None):
        self.model = gameModel
        self.view = gameView

    def init_game(self):
        # TODO Init all game options with GUI
        GameView = GameGuiView()
        self.view = GameView

        # self.view.display_welcome_message()
        # self.view.display_game_options()

        players = [HumanPlayer("Michaël", "X"), HumanPlayer("Jeff", "O")]
        board = Board(players)
        rules = ClassicRules(board, players)
        gameModel = Game(board, rules, players)
        self.view.board_view = BoardGuiView(board)
        self.model = gameModel

        self.view.draw_board(gameModel)  # TODO Remove this line after test and implementing init_game is finish
        self.view.window.mainloop()
        return "success"

    def run_game(self):
        # TODO Run game with options getted from init_game GUI
        pass
