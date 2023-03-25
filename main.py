from tkinter import *


def print_sth():
    print("hello world")


window = Tk()
window.geometry('300x300')
window.title('TK Music Player')

text_label = Label(window, text="Play Button")
text_label.pack()

play_icon = PhotoImage(file="assets/icons/play.png").subsample(5)
play_icon_label = Label(window, image=play_icon)
play_icon_label.pack()

play_btn = Button(window, image=play_icon, command=print_sth)
play_btn.pack()

if __name__ == "__main__":
    window.mainloop()
