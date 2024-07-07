import customtkinter as ctk

class Menu(ctk.CTkFrame):
    def __init__(self, master, board):
        self.main_window = master
        super().__init__(master)
        self.board = board
        self.time_m = 0
        self.time_s = 0
        self.points = 0
        self.game_over = False
        self.next = None
        self.paused = False
        self.timer()
        self.pause_button()
        self.main_window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def timer(self) -> None:
        self.time_label = ctk.CTkLabel(self, font=ctk.CTkFont('Franklin Gothic', 64),
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
        elif not self.paused:
            self.paused = True
        else:
            self.paused = False
            self.update_timer()

    def pause_clicked(self, event) -> None:
        if not self.paused:
            self.main_window.end_game(False)
        else:
            self.main_window.start_game(False)

    def pause_button(self):
        self.pause_label = ctk.CTkLabel(self, font=ctk.CTkFont('Franklin Gothic', 64),
                                        text='\u23F8')
        self.pause_label.pack(side=ctk.RIGHT, padx=10, pady=10)
        self.pause_label.bind('<Button-1>', lambda e: self.pause_clicked(e))

    def restart_timer(self):
        self.time_s = 0
        self.time_m = 0
        self.points = 0

    def on_closing(self):
        if self.next:
            self.master.after_cancel(self.next)
        self.main_window.destroy()
