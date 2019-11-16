#!/usr/bin/env python3

# import standard lib
import os
import sys
from pdb import set_trace
import tkinter as tk

# import custom lib

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
    return 0

if __name__ == '__main__':
    result = main()
    sys.exit(result)
