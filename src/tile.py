import customtkinter as ctk

import random

class Tile(ctk.CTkButton):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.number: int = 0

    def generate_number(self) -> None:
        numbers: list[int] = [2,2,2,2,2,4]
        self.number = random.choice(numbers)
