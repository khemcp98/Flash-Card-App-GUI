from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_I = ("Ariel", 40, "italic")
FONT_B = ("Ariel", 60, "bold")
random_data = {}
data_records = {}

try:
    data = pd.read_csv('data/words_to_learn')
except FileNotFoundError:
    original_data = pd.read_csv('data/Hindi_words.csv')
    data_records = original_data.to_dict(orient='records')
else:
    data_records = data.to_dict(orient='records')


def flip_card():
    canvas.itemconfig(bg_image, image=back_image)
    hi_to_en = random_data['in English']
    canvas.itemconfig(hindi_text, text=hi_to_en, fill='white', font=FONT_B)
    canvas.itemconfig(title, text='English', fill='white', font=FONT_I)


def next_word():
    global random_data, flip_timer
    window.after_cancel(flip_timer)
    random_data = random.choice(data_records)
    canvas.itemconfig(bg_image, image=front_image)
    canvas.itemconfig(hindi_text, text=random_data['Hindi'], fill='black', font=FONT_B)
    canvas.itemconfig(title, text='Hindi', fill='black')
    flip_timer = window.after(3000, flip_card)


def click_right():
    data_records.remove(random_data)
    new_data = pd.DataFrame(data_records)
    new_data.to_csv('data/words_to_learn.csv', index=False)
    next_word()


window = Tk()
window.config(padx=25, pady=25, bg=BACKGROUND_COLOR)
window.title('Flash Card')
flip_timer = window.after(3000, flip_card)

front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
right_bt_img = PhotoImage(file='images/right.png')
wrong_bt_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text='title', font=FONT_I)
hindi_text = canvas.create_text(400, 280, text='word', font=('mangal', 60))

right_button = Button(image=right_bt_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=click_right)
right_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_bt_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_word)
wrong_button.grid(row=1, column=0)

next_word()

window.mainloop()
