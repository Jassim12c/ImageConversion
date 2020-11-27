import os, sys
import tkinter
from PIL import Image


class ImageConv:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg="blue")
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        #  Calling methods
        self.build_grid()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)

if __name__ == "__main__":
    root = tkinter.Tk()
    ImageConv(root)
    root.mainloop()
