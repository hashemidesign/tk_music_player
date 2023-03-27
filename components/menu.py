from tkinter import filedialog, messagebox

import ttkbootstrap as ttk


class MenuBar(ttk.Menu):
    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller

        # menubar = Menu(window)
        file_submenu = ttk.Menu(self, tearoff=0)
        container.config(menu=self)

        self.add_cascade(label="File", menu=file_submenu, underline=0)
        file_submenu.add_command(label="Open", underline=0, command=self.browse_file)
        file_submenu.add_command(label="Exit", command=self.exit)

        help_submenu = ttk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_submenu)
        help_submenu.add_command(label="About", command=self.show_help_window)

    def browse_file(self):
        filename = filedialog.askopenfilename()
        self.controller.set_filename(filename)

    def exit(self):
        self.controller.destroy()

    def show_help_window(self):
        messagebox.showinfo(
            title="About Tk Music Player",
            message="Hello Everyone, This is a revolutionary music player of 21st century",
        )
