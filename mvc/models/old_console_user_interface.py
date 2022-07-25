from models.user_interface import UserInterface


class ConsoleUserInterface(UserInterface):
    def __init__(self, rules, players, player_turn, game_state):
        super().__init__(rules, players, player_turn, game_state)
