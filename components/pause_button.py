import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class PauseButton(ttk.Button):
    def __init__(self, container, controller):
        super().__init__(container, command=controller.pause, text="Pause", style=(OUTLINE, INFO))
