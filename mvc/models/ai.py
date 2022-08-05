from copy import deepcopy

from models.player import Player


class AI(Player):
    difficulty = {
        "1": "easy",
        "2": "medium",
        "3": "hard",
        "4": "very_hard",
    }

    @staticmethod
    def get_ai_difficulty_name_from_choice(choice):
        if choice in AI.difficulty:
            return AI.difficulty[choice]
        # NOTE Always return easy mode if no corresponding choice is finded (just in case)
        return "easy"

    @staticmethod
    def get_ai_difficulty_integer_from_difficulty_name(difficulty_name):
        for key, value in AI.difficulty.items():
            if value == difficulty_name:
                return key
        # NOTE Always return easy mode if no corresponding difficulty_name is finded (just in case)
        return "1"

    def __init__(self, name, symbol, difficulty="medium"):
        super().__init__(name, symbol)
        self.difficulty = difficulty

    def get_move(self, rules):
        return super().get_a_move(rules, int(self.get_ai_difficulty_integer_from_difficulty_name(self.difficulty)))

    # NOTE: This method isn't used anymore, since the easy mode (one depth and no heuristic function) of minimax is doing the same has this method - Just let it here because it was a requirement of the part 3 of this project (before implementing minimax algorithm).
    def get_highest_scored_move(self, rules):
        move_availables = rules.get_valid_moves(self)
        backup_mat = deepcopy(rules.board.mat)
        moves_with_count_symbols_available_for_ia = {}

        for move_available in move_availables:
            row = move_available[0]
            col = move_available[1]
            rules.make_move(row, col, self)
            count_symbols_ia = 0
            for i in range(rules.board.size):
                for j in range(rules.board.size):
                    if rules.board.get_cell(i, j) == self.symbol:
                        count_symbols_ia += 1
            dict_index_formatted = f"{str(row)},{str(col)}"
            moves_with_count_symbols_available_for_ia[dict_index_formatted] = count_symbols_ia
            rules.board.mat = deepcopy(backup_mat)

        move_to_make = ""
        highest_count_symbols = 0
        for move, count_symbols in moves_with_count_symbols_available_for_ia.items():
            if count_symbols > highest_count_symbols:
                highest_count_symbols = count_symbols
                move_to_make = move

        move_to_make = move_to_make.split(",")
        move_to_make[0] = int(move_to_make[0])
        move_to_make[1] = int(move_to_make[1])
        return move_to_make
