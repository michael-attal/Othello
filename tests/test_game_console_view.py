# test_game_console_view.py
import unittest

from mvc.views.game_console_view import GameConsoleView


class TestGameConsoleView(unittest.TestCase):
    def setUp(self):
        self.gameConsoleView = GameConsoleView()

    def test_get_move_with_invalid_value(self):
        with self.assertRaises(ValueError):
            self.gameConsoleView.get_move("best move")

    def test_get_move_with_invalid_tuple_int(self):
        with self.assertRaises():
            self.gameConsoleView.get_move("1, p")
