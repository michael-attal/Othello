import tkinter as tk
from functools import partial


from models.ai import AI
from views.game_view import GameView
from views.board_gui_view import BoardGuiView
from models.game import Game
from models.player import Player


class GameGuiView(GameView):
    def __init__(self, game: Game = None) -> None:
        super().__init__(game)
        self.window = tk.Tk()
        self.window.title("Othello game")
        self.board_view = None
        if game != None:
            self.board_view = BoardGuiView(game.board)

    def get_game_option(self):
        pass

    def handle_game_option(self, player_choice):
        # TODO Implement handle_game_option
        if player_choice == "1":
            pass
        elif player_choice == "2":
            self.display_get_player_name_gui("one", "black")
        else:
            self.window.destroy()

    def get_player_name(self, ent_name: tk.Entry):
        name = ent_name.get()
        return name

    def display_get_player_name_gui(self, player_number, color_disk):
        txt_ask_name_message = tk.Label(text=f"Player {player_number}, please enter your name (you will play {color_disk} disk)")
        txt_ask_name_message.pack()
        ent_name = tk.Entry(fg="yellow", bg="blue", width=50)
        ent_name.pack()
        handle_click_btn_submit_name_with_arg = partial(self.get_player_name, ent_name)
        btn_submit_name = tk.Button(master=self.window, text="Submit", command=handle_click_btn_submit_name_with_arg)
        btn_submit_name.pack()

    def get_ai_difficulty(self):
        pass

    def display_welcome_message(self):
        txt_welcome_message = tk.Label(master=self.window, text="Welcome to Reversi game (Also called Othello)!")
        txt_welcome_message.pack()

    def display_lets_start_the_game_message(self):
        pass

    def display_goodbye_message(self):
        pass

    def display_game_options(self):
        txt_game_options_message = tk.Label(master=self.window, text="Please select one of the below options: ")
        txt_game_options_message.pack()

        handle_click_btn_choice_player_vs_ai_with_arg = partial(self.handle_game_option, "1")
        btn_choice_player_vs_ai = tk.Button(master=self.window, text="Player VS AI", command=handle_click_btn_choice_player_vs_ai_with_arg)
        handle_click_btn_choice_player_vs_player_with_arg = partial(self.handle_game_option, "2")
        btn_choice_player_vs_player = tk.Button(master=self.window, text="Player VS Player", command=handle_click_btn_choice_player_vs_player_with_arg)
        handle_click_btn_choice_quit_game_with_arg = partial(self.handle_game_option, "0")
        btn_choice_quit_game = tk.Button(master=self.window, text="Quit the game", command=handle_click_btn_choice_quit_game_with_arg)

        btn_choice_player_vs_ai.pack()
        btn_choice_player_vs_player.pack()
        btn_choice_quit_game.pack()

    def display_ai_informations_message(self):
        pass

    def display_available_ai_difficulties(self):
        pass

    def get_move(self, curr_player: Player):
        pass

    def draw_board(self, game):
        self.board_view.draw_board(self.window, game.rules, game.players)

    def display_invalid_game_option_selected(self):
        pass

    def display_invalid_game_option_selected(self):
        pass

    def display_not_valid_move(self):
        pass

    def display_ia_move(self, row, col):
        pass

    def display_winner(self, player: Player):
        pass

    def display_no_winner(self, player: Player):
        pass
