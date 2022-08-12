from controllers.game_console_controller import GameConsoleController
from controllers.game_gui_controller import GameGuiController


controllerConsole = GameConsoleController()
controllerGui = GameGuiController()  # NOTE: Still not implemented (will only display available cases and current disks players on the board)
controller = controllerConsole

# NOTE: Get the information needed to start the game, like player name and opponent...
game_option_selected = controller.init_game()
# NOTE: If the user has not selected to exit the game and if no error occurs during the initialization of the game, then start the game.
if game_option_selected != "exit" and game_option_selected != "error":
    controller.run_game()
