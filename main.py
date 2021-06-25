from tkinter import *

import pandas as pd
import random


class Typer(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Typer")
        self.geometry("610x210")
        main_frame = Frame(self)
        self.frames = {
            "typer": TypeFrame(self),
            "words": WordsFrame(self),
            "results": ResultsFrame(self)
        }

        self.show_typer_statistics()
        main_frame.config(bg="#ffffff")
        main_frame.pack(fill=BOTH, expand=True)

    def show_frame(self, name):
        frame = self.frames[name]
        frame.config(bg="#f1f1f1")
        frame.place(width=600, height=200, relx=0.5, rely=0.5, anchor=CENTER)
        frame.tkraise()

    def show_typer_statistics(self):
        self.show_frame("words")
        self.show_frame("typer")

    def show_results_frame(self):
        self.show_frame("results")


class TypeFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # row 0
        Label(self, text="Corrected CPM:").grid(row=0, column=0)
        cpm_calculated_text = StringVar()
        cpm_calculated_text.set("TBD")
        Entry(self, textvariable=cpm_calculated_text, state='disabled').grid(row=0, column=1)

        Label(self, text="WPM:").grid(row=0, column=2)
        wpm_calculated_text = StringVar()
        wpm_calculated_text.set("TBD")
        Entry(self, textvariable=wpm_calculated_text, state='disabled').grid(row=0, column=3)

        Label(self, text="Time left:").grid(row=0, column=4)
        time_left_int_text = IntVar()
        time_left_int_text.set(60)
        Entry(self, textvariable=time_left_int_text, state='disabled').grid(row=0, column=5)

        restart_button_text = StringVar()
        restart_button_text.set("Restart")
        Button(self, textvariable=restart_button_text, fg="red", relief=FLAT).grid(row=0, column=6)

        # row 2
        typing_area_text = StringVar()
        typing_area_text.set("type the words here")
        Entry(self, textvariable=typing_area_text).grid(row=2, column=0, columnspan=6)


class WordsFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        words = pd.read_csv("words.txt").values()

        frame = Frame(self, bg="#ffffff")
        Label(self, text=words).tkraise()


class ResultsFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(parent)
        pass


if __name__ == "__main__":
    app = Typer()
    app.mainloop()
