from tkinter import *

class Application:
    def __init__(self, master=None):
        self.setor1 = Frame(master)
        self.setor1.pack(fill=X)

root = Tk()
Application(root)
root.mainloop()