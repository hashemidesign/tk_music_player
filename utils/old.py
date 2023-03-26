import tkinter
from tkinter import *
from tkinter import filedialog, messagebox

from pygame import mixer

filename = ''
is_playing = False


def browse_file():
    global filename
    filename = filedialog.askopenfilename()


def show_help_window():
    tkinter.messagebox.showinfo(
        title="About Tk Music Player",
        message="Hello Everyone, This is a revolutionary music player of 21st century",
    )


window = Tk()
mixer.init()
window.geometry('500x500')
window.title('TK Music Player')

menubar = Menu(window)
file_submenu = Menu(menubar, tearoff=0)
window.config(menu=menubar)

menubar.add_cascade(label="File", menu=file_submenu, underline=0)
file_submenu.add_command(label="Open", underline=0, command=browse_file)
file_submenu.add_command(label="Exit", command=window.destroy)

help_submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_submenu)
help_submenu.add_command(label="About", command=show_help_window)


def play_music():
    global is_playing
    try:
        mixer.music.load(filename)
        mixer.music.play()
        is_playing = True
    except:
        tkinter.messagebox.showerror("File Not Found")
        print("File Not Found Error")


def stop_music():
    global is_playing
    mixer.music.stop()
    is_playing = False


def pause_music():
    global is_playing
    try:
        if is_playing:
            mixer.music.pause()
            is_playing = False
        else:
            mixer.music.unpause()
            is_playing = True
    except:
        tkinter.messagebox.showerror("File Not Found")
        print("File Not Found Error")


def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)


def prev_music():
    pass


def next_music():
    pass


text_label = Label(window, text="Play Button")
text_label.pack()

play_icon = PhotoImage(file="assets/icons/96/play.png")
stop_icon = PhotoImage(file="assets/icons/96/stop.png")
pause_icon = PhotoImage(file="assets/icons/96/pause.png")
next_icon = PhotoImage(file="assets/icons/96/forward.png")
prev_icon = PhotoImage(file="assets/icons/96/rewind.png")

top_frame = Frame(window)
top_frame.pack(padx=10, pady=10)

prev_btn = Button(top_frame, image=prev_icon, command=prev_music)
prev_btn.grid(row=0, column=0, padx=10)

play_btn = Button(top_frame, image=play_icon, command=play_music)
play_btn.grid(row=0, column=1, padx=10)

pause_btn = Button(top_frame, image=pause_icon, command=pause_music)
pause_btn.grid(row=0, column=2, padx=10)

stop_btn = Button(top_frame, image=stop_icon, command=stop_music)
stop_btn.grid(row=0, column=3, padx=10)

next_btn = Button(top_frame, image=next_icon, command=next_music)
next_btn.grid(row=0, column=4, padx=10)

scale = Scale(top_frame, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(30)
scale.grid(row=1, column=0, columnspan=5, pady=15, sticky=NSEW)

bottom_frame = Frame(window)
bottom_frame.pack(padx=10, pady=10)

status_bar = Label(window, text="Keep Enjoying the Music", relief=SUNKEN, anchor=W)
status_bar.pack(side=BOTTOM, fill=X)

if __name__ == "__main__":
    window.mainloop()
