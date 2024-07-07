import customtkinter as ctk
import random

from properties import SIZES, COLOR
from tile import Tile

class Board(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.board = self.create_board()
        self.display_board()
        self.new_tile()

    def create_board(self) -> list[list[Tile]]:
        return [[Tile(self) for _ in range(4)] for _ in range(4)]

    def new_tile(self) -> None:
        if not self.check_space():
            return
        x = random.randrange(0, 4)
        y = random.randrange(0, 4)
        while self.board[x][y].number:
            x = random.randrange(0, 4)
            y = random.randrange(0, 4)
        self.board[x][y].generate_number()
        self.update_board()

    def check_space(self) -> bool:
        for row in self.board:
            for tile in row:
                if not tile.number:
                    return True
        return False

    def display_board(self):
        self.board_matrix = [[None for _ in range(4)] for _ in range(4)]
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                tile_frame = ctk.CTkLabel(self, width=int(SIZES.CELL_WIDTH),
                                        height=int(SIZES.CELL_HEIGHT),
                                        text=f'{tile.number}', fg_color= COLOR.GRAY,
                                        corner_radius=10, font=ctk.CTkFont('Franklin Gothic', 21))
                tile_frame.grid(column=j, row=i, sticky=ctk.NSEW, padx=5, pady=5)
                self.board_matrix[i][j] = tile_frame

    def update_board(self):
        for i, row in enumerate(self.board_matrix):
            for j, tile in enumerate(row):
                tile.configure(text=f'{self.board[i][j].number}')
                if self.board[i][j].number > 4:
                    tile.configure(fg_color = COLOR.GREEN)
                elif self.board[i][j].number > 32:
                    tile.configure(fg_color = COLOR.ORANGE)
                elif self.board[i][j].number > 256:
                    tile.configure(fg_color = COLOR.RED)

    def move_up(self, event):
        for _ in range(3):
            for i, row in enumerate(self.board):
                for j, tile in enumerate(row):
                    if not i:
                        continue
                    if self.board[i][j].number and not self.board[i-1][j].number:
                        self.board[i-1][j].number = self.board[i][j].number
                        self.board[i][j].number = 0
                    elif (self.board[i][j].number == self.board[i-1][j].number) and self.board[i][j].number:
                        self.board[i-1][j].number = self.board[i][j].number * 2
                        self.board[i][j].number = 0
        self.new_tile()
        self.update_board()

    def move_down(self, event):
        self.update_board()

    def move_right(self, event):
        self.update_board()

    def move_left(self, event):
        self.update_board()
