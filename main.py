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
        self.build_banner()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.columnconfigure(2, weight=0)
        self.mainframe.rowconfigure(0, weight=0)
        self.mainframe.rowconfigure(1, weight=1)

    def build_banner(self):
        banner = tkinter.Label(
            self.mainframe,
            text="Image Conversion",
            bg="blue",
            fg="black",
            font=("Courier", 24)
        )
        banner.grid(
            row=0, column=1,
            sticky="ew",
            padx=10, pady=10,
        )

if __name__ == "__main__":
    root = tkinter.Tk()
    ImageConv(root)
    root.mainloop()


