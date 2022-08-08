# test_ai.py
import unittest
from mvc.models.board import Board
from mvc.models.classic_rules import ClassicRules
from mvc.models.player import Player
from mvc.models.ai import AI


class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI("Terminator", "O", "medium")
        self.players = []
        self.players.append(Player("Michaël", "X"))
        self.players.append(self.ai)
        self.board = Board(self.players)
        self.rules = ClassicRules(self.board, self.players)

    def test_get_ai_difficulty_name_from_choice_with_invalid_value(self):
        self.assertEqual(self.ai.get_ai_difficulty_name_from_choice("99"), "easy")

    def test_get_ai_difficulty_name_from_choice_with_valid_value(self):
        self.assertEqual(self.ai.get_ai_difficulty_key_from_difficulty_value("very_hard"), "4")

    def test_get_highest_scored_move(self):
        self.assertEqual(self.ai.get_highest_scored_move(self.rules), [2, 4])

    def test_get_move(self):
        self.assertEqual(self.ai.get_move(self.rules), (5, 3))
