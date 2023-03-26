import tkinter as tk
from tkinter import ttk


class TkMusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tk Music Player")
        self.geometry("640x480")


if __name__ == "__main__":
    tkMusicPlayer = TkMusicPlayer()
    style = ttk.Style(tkMusicPlayer)


    tkMusicPlayer.mainloop()
