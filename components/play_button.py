import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class PlayButton(ttk.Button):
    def __init__(self, container, controller):
        super().__init__(container, command=controller.play, text="Play", style=(OUTLINE, INFO))
