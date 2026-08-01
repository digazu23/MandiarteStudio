<<<<<<< HEAD
"""Pendiente"""
=======
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MandiarteStudio")
        self.geometry("800x600")
        label = ttk.Label(self, text="MandiarteStudio - UI placeholder")
        label.pack(padx=20, pady=20)


def run():
    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    run()
>>>>>>> 6eb822cc94213bf390d7c5b94e4d23cab996c31a
