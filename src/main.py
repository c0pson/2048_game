import customtkinter as ctk
import sys
import os

from menu import Menu, ScoreTable
from board import Board

from properties import COLOR

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__(fg_color=COLOR.BACKGROUND)
        self.binds: list[str] = ['<Up>', '<Down>', '<Right>', '<Left>']
        self.score_table = ScoreTable(self)
        self.board = Board(self)
        self.menu = Menu(self, self.board)
        self.menu.pack(padx=10, pady=10, fill='x')
        self.board.pack(expand=True, padx=10, pady=10)
        self.score_table.pack(padx=10, pady=10, fill='x')
        self.bind('<Up>', lambda e: self.board.move_up(e, 1))
        self.bind('<Down>', lambda e: self.board.move_down(e, 1))
        self.bind('<Right>', lambda e: self.board.move_right(e, 1))
        self.bind('<Left>', lambda e: self.board.move_left(e, 1))

    def end_game(self, over) -> None:
        self.menu.pause_start(None, False)
        if over:
            self.menu.game_over = True
            self.menu.disable_undo()
        for bind in self.binds:
            self.unbind(bind)

    def start_game(self, restart_: bool) -> None:
        self.bind('<Up>', lambda e: self.board.move_up(e, 1))
        self.bind('<Down>', lambda e: self.board.move_down(e, 1))
        self.bind('<Right>', lambda e: self.board.move_right(e, 1))
        self.bind('<Left>', lambda e: self.board.move_left(e, 1))
        self.menu.pause_start(None, restart=restart_)
        if restart_:
            self.score_table.points = 0
            self.score_table.update_score()
            self.menu.enable_undo()

    def unlock(self) -> None:
        self.menu.game_over = False

    def update_score(self, point: int) -> None:
        self.score_table.points += point
        self.score_table.update_score()

if __name__ == "__main__":
    window = MainWindow()
    window.geometry('720x940')
    window.minsize(720, 940)
    window.title('2048')
    if os.name == 'nt':
        window.after(201, window.iconbitmap(resource_path('img\\logo.ico')))
    else:
        window.after(201, window.iconbitmap(resource_path('img/logo.ico')))
    window.mainloop()
