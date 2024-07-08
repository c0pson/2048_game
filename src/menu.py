import customtkinter as ctk
import sys
import os

from properties import COLOR

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Menu(ctk.CTkFrame):
    def __init__(self, master, board):
        self.main_window = master
        super().__init__(master, fg_color=COLOR.FOREGROUND)
        ctk.FontManager.windows_load_font(resource_path('fonts\\NotoEmoji-VariableFont_wght.ttf'))
        ctk.FontManager.windows_load_font(resource_path('fonts\\Poppins-Black.ttf'))
        self.board = board
        self.time_m = 0
        self.time_s = 0
        self.points = 0
        self.game_over = False
        self.next = None
        self.paused = False
        self.timer()
        self.pause_button()
        self.restart_button()
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def timer(self) -> None:
        self.time_label = ctk.CTkLabel(self, font=ctk.CTkFont('Poppins', 64), text_color=COLOR.TEXT_2, 
                                        text=f'{str(self.time_m).zfill(2)}:{str(self.time_s).zfill(2)}')
        self.time_label.pack(side=ctk.LEFT, padx=10, pady=10)
        self.next = self.master.after(1000, self.update_timer)

    def update_timer(self) -> None:
        if not self.paused:
            self.time_s += 1
            if self.time_s == 60:
                self.time_s = 0
                self.time_m += 1
            if self.time_m > 99:
                self.time_m = 0
                self.time_s = 0
            self.time_label.configure(text=f'{str(self.time_m).zfill(2)}:{str(self.time_s).zfill(2)}')
            self.next = self.master.after(1000, self.update_timer)

    def pause_start(self, event, restart: bool) -> None:
        if self.game_over:
            return
        elif restart:
            self.paused = False
            self.restart_timer()
            self.update_timer()
            self.paused_label.destroy()
        elif not self.paused:
            self.paused = True
            self.paused_frame()
        else:
            self.paused = False
            self.update_timer()
            self.paused_label.destroy()

    def pause_clicked(self, event) -> None:
        if not self.paused:
            self.main_window.end_game(False)
        else:
            self.main_window.start_game(False)

    def pause_button(self):
        self.pause_label = ctk.CTkLabel(self, text='⏸️', font=ctk.CTkFont('Noto Emoji', 64),
                                        text_color=COLOR.ACCENT)
        self.pause_label.pack(side=ctk.RIGHT, padx=10, pady=10)
        self.pause_label.bind('<Button-1>', lambda e: self.pause_clicked(e))

    def paused_frame(self):
        self.paused_label = ctk.CTkLabel(self.master, text='PAUSED',
                                        font=ctk.CTkFont('Poppins', 64),
                                        text_color=COLOR.ACCENT)
        self.paused_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER, relwidth=1)

    def restart_timer(self):
        self.time_s = 0
        self.time_m = 0
        self.points = 0

    def restart_button(self):
        self.restart_label = ctk.CTkLabel(self, text='🔃', font=ctk.CTkFont('Noto Emoji', 64),
                                            text_color=COLOR.ACCENT)
        self.restart_label.pack(side=ctk.RIGHT, padx=10, pady=10)
        self.restart_label.bind('<Button-1>', lambda e: self.restart(e))

    def restart(self, event):
        self.board.new_game()

    def on_closing(self):
        if self.next:
            self.master.after_cancel(self.next)
        self.main_window.destroy()

class ScoreTable(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=COLOR.FOREGROUND)
        self.points = 0
        self.score_table()

    def score_table(self):
        self.score_label = ctk.CTkLabel(self, text=f'Score: {self.points}', font=ctk.CTkFont('Poppins', 64),
                                            text_color=COLOR.ACCENT)
        self.score_label.pack(side=ctk.LEFT, padx=10, pady=10)

    def update_score(self):
        self.score_label.configure(text=f'Score: {self.points}')

    def restart_score(self):
        self.points = 0
