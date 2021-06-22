from tkinter import *
import pandas as pd
import random

# goal = "https://typing-speed-test.aoeu.eu/?lang=en"

# initialize application
root = Tk()
root.title("Typist Test")


class TypistTest:
    def __init__(self):
        pass

    def words_to_type(self):
        data = pd.read_csv("words.txt")
        data_dict = data.to_dict()
        for word in data_dict:
            current_word = random.choice(word)
            print(current_word)


    def cpm_calc(self):
        pass

    def wpm_calc(self):
        pass

    def test_time(self, time_left=60):
        for i in range(time_left):
            time_left -= i
            time_left_int_text.set(time_left)


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

TypistTest().words_to_type()
root.mainloop()
