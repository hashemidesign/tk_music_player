import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class StopButton(ttk.Button):
    def __init__(self, container, controller):
        super().__init__(container, command=controller.stop, text="Stop", style=(OUTLINE, INFO))
