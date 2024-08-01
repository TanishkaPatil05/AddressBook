import tkinter as Tk


class About_Window(object):

    def __init__(self, master):
        top = self.top = Tk.Toplevel(master)
        self.master = master
        top.title("About Us")

        self.label = Tk.Label(top, text="Address Book Management System")
        self.label.grid(row=1, column=0, padx=10, pady=10)
