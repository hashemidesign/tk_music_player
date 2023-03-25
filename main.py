import tkinter
from tkinter import *
from pygame import mixer
from tkinter import filedialog, messagebox


filename = ''


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
    try:
        mixer.music.load(filename)
        mixer.music.play()
    except:
        tkinter.messagebox.showerror("File Not Found")
        print("File Not Found Error")


def stop_music():
    mixer.music.stop()


def pause_music():
    mixer.music.pause()


def set_volume(value):
    volume = int(value) / 100
    mixer.music.set_volume(volume)


text_label = Label(window, text="Play Button")
text_label.pack()

play_icon = PhotoImage(file="assets/icons/96/play.png")
stop_icon = PhotoImage(file="assets/icons/96/stop.png")
pause_icon = PhotoImage(file="assets/icons/96/pause.png")
next_icon = PhotoImage(file="assets/icons/96/forward.png")
prev_icon = PhotoImage(file="assets/icons/96/rewind.png")

play_btn = Button(window, image=play_icon, command=play_music)
play_btn.pack()

pause_btn = Button(window, image=pause_icon, command=pause_music)
pause_btn.pack()

stop_btn = Button(window, image=stop_icon, command=stop_music)
stop_btn.pack()

scale = Scale(window, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
scale.set(30)
scale.pack()

if __name__ == "__main__":
    window.mainloop()
