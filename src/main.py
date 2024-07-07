import customtkinter as ctk

from tile import Tile
from board import Board

class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        board = Board(self)
        board.pack(expand=True, padx=10, pady=10)
        self.bind('<Up>', lambda e: board.move_up(e, 1))
        self.bind('<Down>', lambda e: board.move_down(e, 1))
        self.bind('<Right>', lambda e: board.move_right(e, 1))
        self.bind('<Left>', lambda e: board.move_left(e, 1))

if __name__ == "__main__":
    window = MainWindow()
    window.geometry('720x720')
    window.title('2048')
    window.mainloop()
