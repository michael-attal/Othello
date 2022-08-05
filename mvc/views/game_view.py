from abc import ABC, abstractmethod

from models.game import Game


class GameView(ABC):
    def __init__(self, gameModel: Game):
        self.game = gameModel

    @abstractmethod
    def get_game_option(self):
        pass

    @abstractmethod
    def get_ai_difficulty(self):
        pass

    @abstractmethod
    def get_player_name(self):
        pass

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    def display_welcome_message(self):
        pass

    def display_lets_start_the_game_message(self):
        pass

    def display_goodbye_message(self):
        pass

    def display_game_options(self):
        pass

    def display_ai_informations_message(self):
        pass

    def display_available_ai_difficulties(self):
        pass

    def display_invalid_game_option_selected(self):
        pass

    def display_invalid_ai_difficulty_selected(self):
        pass

    @abstractmethod
    def display_not_valid_move(self):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass

    @abstractmethod
    def display_no_winner(self, player):
        pass
