import customtkinter as ctk
from copy import deepcopy
import random

from properties import SIZES, COLOR
from tile import Tile

class Board(ctk.CTkFrame):
    def __init__(self, master) -> None:
        self.main_menu = master
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
        self.check_lose()

    def check_space(self) -> bool:
        for row in self.board:
            for tile in row:
                if not tile.number:
                    return True
        return False

    def display_board(self) -> None:
        self.board_matrix = [[None for _ in range(4)] for _ in range(4)]
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                tile_frame = ctk.CTkLabel(self, width=int(SIZES.CELL_WIDTH),
                                        height=int(SIZES.CELL_HEIGHT),
                                        text=f'{tile.number}', fg_color= COLOR.GRAY,
                                        corner_radius=10, font=ctk.CTkFont('Franklin Gothic', 64))
                tile_frame.grid(column=j, row=i, sticky=ctk.NSEW, padx=5, pady=5)
                self.board_matrix[i][j] = tile_frame

    def update_board(self):
        for i, row in enumerate(self.board_matrix):
            for j, tile in enumerate(row):
                tile.configure(text=f'{self.board[i][j].number}')
                if self.board[i][j].number <= 4:
                    tile.configure(fg_color = COLOR.GRAY)
                elif self.board[i][j].number > 256:
                    tile.configure(fg_color = COLOR.RED)
                elif self.board[i][j].number > 32:
                    tile.configure(fg_color = COLOR.ORANGE)
                elif self.board[i][j].number > 4:
                    tile.configure(fg_color = COLOR.GREEN)

    def check_if_can_move(self, original_boar) -> bool:
        for i, row in enumerate(original_boar):
            for j, tile in enumerate(row):
                if self.board[i][j].number != original_boar[i][j]:
                    return False
        return True

    def sum_up(self) -> None:
        for i, row in enumerate(self.board):
            for j, tile in enumerate(row):
                if not i:
                    continue
                if self.board[i][j].number == self.board[i-1][j].number and self.board[i][j].number:
                    self.board[i-1][j].number *= 2
                    self.board[i][j].number = 0

    def move_up(self, event, iter: int) -> None:
        original_board = [[self.board[j][i].number for i in range(4)] for j in range(4)]
        for _ in range(3):
            for i, row in enumerate(self.board):
                for j, tile in enumerate(row):
                    if not i:
                        continue
                    if self.board[i][j].number and not self.board[i-1][j].number:
                        self.board[i-1][j].number = self.board[i][j].number
                        self.board[i][j].number = 0
        if iter:
            self.sum_up()
            self.move_up(event, iter-1)
            if not self.check_if_can_move(original_board):
                self.new_tile()
            if self.check_lose():
                self.restart()
                return
        self.update_board()

    def sum_down(self) -> None:
        for i in range(len(self.board)-1, -1, -1):
            for j in range(len(self.board[i])):
                if i == len(self.board) - 1:
                    continue
                if self.board[i][j].number == self.board[i+1][j].number and self.board[i][j].number:
                    self.board[i+1][j].number *= 2
                    self.board[i][j].number = 0

    def move_down(self, event, iter: int) -> None:
        original_board = [[self.board[j][i].number for i in range(4)] for j in range(4)]
        for _ in range(3):
            for i in range(len(self.board)-1, -1, -1):
                for j in range(len(self.board[i])):
                    if i == len(self.board) - 1:
                        continue
                    if self.board[i][j].number and not self.board[i+1][j].number:
                        self.board[i+1][j].number = self.board[i][j].number
                        self.board[i][j].number = 0
        if iter:
            self.sum_down()
            self.move_down(event, iter-1)
            if not self.check_if_can_move(original_board):
                self.new_tile()
            if self.check_lose():
                self.restart()
                return
        self.update_board()

    def sum_right(self):
        for i, row in enumerate(self.board):
            for j in range(len(row)-1, -1, -1):
                if j == len(row) - 1:
                    continue
                if self.board[i][j].number == self.board[i][j+1].number and self.board[i][j].number:
                    self.board[i][j+1].number *= 2
                    self.board[i][j].number = 0

    def move_right(self, event, iter: int) -> None:
        original_board = [[self.board[j][i].number for i in range(4)] for j in range(4)]
        for _ in range(3):
            for i, row in enumerate(self.board):
                for j in range(len(row)-1, -1, -1):
                    if j == len(row) - 1:
                        continue
                    if self.board[i][j].number and not self.board[i][j+1].number:
                        self.board[i][j+1].number = self.board[i][j].number
                        self.board[i][j].number = 0
        if iter:
            self.sum_right()
            self.move_right(event, iter-1)
            if not self.check_if_can_move(original_board):
                self.new_tile()
            if self.check_lose():
                self.restart()
                return
        self.update_board()


    def sum_left(self):
        for i, row in enumerate(self.board):
            for j in range(len(row)):
                if not j:
                    continue
                if self.board[i][j].number == self.board[i][j-1].number and self.board[i][j].number:
                    self.board[i][j-1].number *= 2
                    self.board[i][j].number = 0

    def move_left(self, event, iter: int) -> None:
        original_board = [[self.board[j][i].number for i in range(4)] for j in range(4)]
        for _ in range(3):
            for i, row in enumerate(self.board):
                for j in range(len(row)):
                    if not j:
                        continue
                    if self.board[i][j].number and not self.board[i][j-1].number:
                        self.board[i][j-1].number = self.board[i][j].number
                        self.board[i][j].number = 0
        if iter:
            self.sum_left()
            self.move_left(event, iter-1)
            if not self.check_if_can_move(original_board):
                self.new_tile()
            if self.check_lose():
                self.restart()
                return
        self.update_board()

    def check_win(self):
        for i, row in enumerate(self.board):
                for j in range(len(row)):
                    if self.board[i][j].number == 2048:
                        print('u won')

    def check_lose(self) -> bool:
        original_board = [[self.board[j][i].number for i in range(4)] for j in range(4)]
        rows = len(original_board)
        cols = len(original_board[0])
        for i in range(rows):
            for j in range(cols):
                current_number = original_board[i][j]
                if current_number == 0:
                    return False
                if j > 0 and original_board[i][j - 1] == current_number:
                    return False
                if j < cols - 1 and original_board[i][j + 1] == current_number:
                    return False
                if i > 0 and original_board[i - 1][j] == current_number:
                    return False
                if i < rows - 1 and original_board[i + 1][j] == current_number:
                    return False
        return True

    def restart(self):
        self.main_menu.end_game(True)
        self.end_frame = ctk.CTkFrame(self)
        self.end_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=1)
        self.notification = ctk.CTkLabel(self.end_frame, font=ctk.CTkFont('Franklin Gothic', 94),
                                        text='GAME OVER')
        self.notification.pack(padx=10, pady=10)
        self.restart_button = ctk.CTkButton(self.end_frame, font=ctk.CTkFont('Franklin Gothic', 94),
                                        text='Restart', command=lambda: self.new_game(),
                                        fg_color=COLOR.GRAY)
        self.restart_button.pack()

    def new_game(self):
        self.board = self.create_board()
        self.new_tile()
        self.end_frame.destroy()
        self.main_menu.unlock()
        self.main_menu.start_game(True)