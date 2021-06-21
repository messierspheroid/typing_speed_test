from tkinter import *
import pandas as pd
import random

# initialize application
root = Tk()
root.title("Typist Test")


class TypistTest:
    def __init__(self, words_output_file, timer):
        self.words = words_output_file
        self.timer = timer

    def txt_to_csv(self):
        words_input_file = pd.read_csv("words.txt", mode="r")
        words_output_file = words_input_file.to_csv("words.csv")

    def words_to_type(self):
        pass

    def cpm_calc(self):
        pass

    def wpm_calc(self):
        pass

    def timer(self):
        pass

# row 0
corrected_cpm_label = Label(root, text="Corrected CPM:")
corrected_cpm_label.grid(row=0, column=0)

cpm_calculated_text = StringVar()
cpm_calculated = Entry(root, textvariable=cpm_calculated_text, state='disabled')
cpm_calculated_text.set("?")
cpm_calculated.grid(row=0, column=1)

wpm_label = Label(root, text="WPM:")
wpm_label.grid(row=0, column=2)

wpm_calculated_text = StringVar()
wpm_calculated = Entry(root, textvariable=wpm_calculated_text, state='disabled')
wpm_calculated_text.set("?")
wpm_calculated.grid(row=0, column=3)

time_left_label = Label(root, text="Time left:")
time_left_label.grid(row=0, column=4)

time_left_int_text = IntVar()
time_left_int = Entry(root, textvariable=time_left_int_text, state='disabled')
time_left_int_text.set(60)
time_left_int.grid(row=0, column=5)

restart_button_text = StringVar()
restart_button = Button(root, textvariable=restart_button_text, fg="red", relief=FLAT)
restart_button_text.set("Restart")
restart_button.grid(row=0, column=6)

# row 1
words_to_type = Frame(root)
words_to_type.grid(row=1, column=0, columnspan=6)

# row 2
typing_area_text = StringVar()
typing_area = Entry(root, textvariable=typing_area_text)
typing_area_text.set("type the words here")
typing_area.grid(row=2, column=0, columnspan=6)

root.mainloop()
