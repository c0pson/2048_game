import customtkinter as ctk

from tile import Tile
from board import Board

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        board = Board(self)
        board.pack(expand=True, padx=10, pady=10)
        self.bind('<Up>', lambda e: board.move_up(e))
        self.bind('<Down>', lambda e: board.move_down(e))
        self.bind('<Right>', lambda e: board.move_right(e))
        self.bind('<Left>', lambda e: board.move_left(e))

if __name__ == "__main__":
    window = MainWindow()
    window.geometry('720x720')
    window.title('2048')
    window.mainloop()
