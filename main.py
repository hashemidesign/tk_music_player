import tkinter as tk

import ttkbootstrap as ttk
from pygame import mixer
from ttkbootstrap.toast import ToastNotification

from components import MenuBar, ControlsFrame


class TkMusicPlayer(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Tk Music Player")
        self.geometry("640x480")

        self.mixer = mixer
        self.mixer.init()
        self.filename = tk.StringVar()
        self.is_playing = tk.BooleanVar(value=False)

        menu = MenuBar(self, self)

        controls_container = ControlsFrame(self, self)
        controls_container.pack()

        status_bar = ttk.Label(self, text="Keep Enjoying the Music", relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_filename(self, fn):
        self.filename.set(fn)

    def play(self):
        try:
            self.mixer.music.load(self.filename.get())
            self.mixer.music.play()
            self.is_playing.set(True)
        except Exception as e:
            toast = ToastNotification(
                title="NO MEDIA",
                message="No music file selected! please select a music first",
                duration=3000,
                bootstyle="danger",
                position=(100, 100, "ne")
            )
            toast.show_toast()
            print(e)

    def stop(self):
        self.mixer.music.stop()
        self.is_playing.set(False)

    def pause(self):
        try:
            if self.is_playing.get():
                self.mixer.music.pause()
                self.is_playing.set(False)
            else:
                self.mixer.music.unpause()
                self.is_playing.set(True)
        except Exception as e:
            toast = ToastNotification(
                title="NO MEDIA",
                message="No music file selected! please select a music first",
                duration=3000,
                bootstyle="danger",
                position=(100, 100, "ne")
            )
            toast.show_toast()
            print(e)

    def set_volume(self, value):
        volume = int(value) / 100
        self.mixer.music.set_volume(volume)


if __name__ == "__main__":
    tkMusicPlayer = TkMusicPlayer()
    tkMusicPlayer.style.theme_use("sandstone")

    tkMusicPlayer.mainloop()
