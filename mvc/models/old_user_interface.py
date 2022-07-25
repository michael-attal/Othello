from abc import ABC, abstractclassmethod


class UserInterface(ABC):
    def __init__(self, rules, players, player_turn, game_state):
        self.rules = rules
        self.players = players
        self.player_turn = player_turn
        self.game_state = game_state
