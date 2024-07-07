import customtkinter as ctk

from board import Board
from menu import Menu

class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.board = Board(self)
        self.binds = ['<Up>', '<Down>', '<Right>', '<Left>']
        self.menu = Menu(self, self.board)
        self.menu.pack(padx=10, pady=10, fill='x')
        self.board.pack(expand=True, padx=10, pady=10)
        self.bind('<Up>', lambda e: self.board.move_up(e, 1))
        self.bind('<Down>', lambda e: self.board.move_down(e, 1))
        self.bind('<Right>', lambda e: self.board.move_right(e, 1))
        self.bind('<Left>', lambda e: self.board.move_left(e, 1))

    def end_game(self, over):
        self.menu.pause_start(None, False)
        if over:
            self.menu.game_over = True
        for bind in self.binds:
            self.unbind(bind)

    def start_game(self, restart_: bool):
        self.bind('<Up>', lambda e: self.board.move_up(e, 1))
        self.bind('<Down>', lambda e: self.board.move_down(e, 1))
        self.bind('<Right>', lambda e: self.board.move_right(e, 1))
        self.bind('<Left>', lambda e: self.board.move_left(e, 1))
        self.menu.pause_start(None, restart=restart_)

    def unlock(self):
        self.menu.game_over = False

if __name__ == "__main__":
    window = MainWindow()
    window.geometry('720x840')
    window.title('2048')
    window.mainloop()
