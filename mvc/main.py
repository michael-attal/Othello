from controllers.game_controller import GameController


controller = GameController("console")

# NOTE: Get the information needed to start the game, like player name and opponent...
game_option_selected = controller.init_game()
# NOTE: If the user has not selected to exit the game and if no error occurs during the initialization of the game, then start the game.
if game_option_selected != "exit" and game_option_selected != "error":
    controller.run_game()
