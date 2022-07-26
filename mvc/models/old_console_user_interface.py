from models.old_user_interface import UserInterface
from models.player import Player


class ConsoleUserInterface(UserInterface):
    def __init__(self, rules, players: list[Player], player_turn, game_state):
        super().__init__(rules, players, player_turn, game_state)
