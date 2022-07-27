from models.game import Game
from models.board import Board
from models.human_player import HumanPlayer
from models.classic_rules import ClassicRules
from models.ia import IA

from views.game_console_view import GameConsoleView
from controllers.game_controller import GameController

players = []
players.append(HumanPlayer("Michaël", "X"))
players.append(IA("Terminator", "O", "easy"))
# players.append(HumanPlayer("Jeff", "O"))
board = Board(8, players)
rules = ClassicRules(board, players)
gameModel = Game(board, rules, players)
GameView = GameConsoleView(gameModel)
controller = GameController(gameModel, GameView)

controller.run_game()
