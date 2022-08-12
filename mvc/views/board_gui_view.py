import tkinter as tk
from functools import partial

from views.board_view import BoardView
from models.board import Board


class BoardGuiView(BoardView):
    def __init__(self, board: Board):
        super().__init__(board)
        self.rules = None

    def handle_click_btn_case(self, btn_case_idx_clicked, rules, curr_player):
        # TODO Implement this method
        print("The button was clicked! Index:", btn_case_idx_clicked)
        row, col = int(btn_case_idx_clicked[0]), int(btn_case_idx_clicked[2])
        if rules.is_valid_move(row, col, curr_player):
            rules.make_move(row, col, curr_player)

    def draw_board(self, window: tk.Tk, rules, players):

        buttons = []
        for i in range(self.board.size):
            window.columnconfigure(i, weight=1, minsize=50)
            window.rowconfigure(i, weight=1, minsize=25)

            for j in range(self.board.size):
                cell = self.board.get_cell(i, j)

                frm_board = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
                frm_board.grid(row=i, column=j, padx=5, pady=5)
                btn_case_idx_clicked = f"{i},{j}"

                display_empty_case = False
                curr_player = players[0]  # TODO Change current player when button clicked

                if cell == "X":
                    photo = tk.PhotoImage(file=r"/Users/michaelattal/Downloads/black_disk.png")
                    photoimage = photo.subsample(2000, 2000)
                elif cell == "O":
                    photo = tk.PhotoImage(file=r"/Users/michaelattal/Downloads/white_disk.png")
                    photoimage = photo.subsample(2000, 2000)
                else:
                    # TODO Show available moves with another condition (get move availables with rules)
                    display_empty_case = True

                if display_empty_case == False:
                    btn_case = tk.Button(master=frm_board, width=9, height=6, bg="green", image=photoimage)
                    btn_case["state"] = "disabled"
                else:
                    handle_click_btn_case_with_arg = partial(self.handle_click_btn_case, btn_case_idx_clicked, rules, curr_player)
                    btn_case = tk.Button(master=frm_board, text=f"({i}, {j})", width=9, height=6, bg="green", command=handle_click_btn_case_with_arg)
                btn_case.pack()
                buttons.append(btn_case)
        window.mainloop()
