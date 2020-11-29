import os, sys
import tkinter

from tkinter import filedialog
from PIL import Image


class ImageConv:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.Frame(self.master, bg="black")
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        #  Calling methods
        self.build_grid()
        self.build_banner()
        self.build_button()

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
            bg="black",
            fg="white",
            font=("Courier", 24)
        )
        banner.grid(
            row=0, column=1,
            sticky="ew",
            padx=10, pady=10,
        )

    def build_button(self):
        button_frame = tkinter.Frame(self.mainframe)
        button_frame.grid(row=1, column=0, padx=10, pady=10)

        self.button_png = tkinter.Button(
            self.mainframe,
            text="Convert to PNG",
            font=("Courier", 20),
        )

        self.button_jpeg = tkinter.Button(
            self.mainframe,
            text="Convert to JPEG",
            font=("Courier", 20),
            command=self.convert_to_jpeg,
        )

        self.button_png.grid(row=1, column=0)
        self.button_jpeg.grid(row=1, column=2)

    def convert_to_jpeg(self):
        """Get png file and convert it to jpeg"""
        root.filename = filedialog.askopenfile(initialdir="/", title="Select file", filetypes=
        (("png files", "*.png"), ("all files", "*.*")))
        r, f = os.path.splitext(root.filename.name)
        print(f)


if __name__ == "__main__":
    root = tkinter.Tk()
    ImageConv(root)
    root.mainloop()
