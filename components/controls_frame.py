import ttkbootstrap as ttk

from components import PlayButton, PauseButton, StopButton


class ControlsFrame(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container, padding=10)

        play_button = PlayButton(self, controller)
        pause_button = PauseButton(self, controller)
        stop_button = StopButton(self, controller)
        play_button.grid(row=0, column=0, sticky="EW")
        pause_button.grid(row=0, column=1, sticky="EW", padx=10)
        stop_button.grid(row=0, column=2, sticky="EW")
