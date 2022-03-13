import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random
def test():
    canvas.itemconfig(test_text,text='it works (:')

def clean_text():
    canvas.delete('label_x')
    card_pickup()


def card_pickup():
    b = data_game_dict[random.randint(0, 99)]['French']
    canvas.create_text(400, 290, text=b, font=("Ariel", 40, "bold"), tags='label_x')
    return b


window = tk.Tk()

# UI STAGE 1
BACKGROUND_COLOR = "#B1DDC6"
window.title("FLASH CARD GAME")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
# front card
canvas = tk.Canvas(window, width=800, height=526)
photo = tk.PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=photo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# create texts

test_text=canvas.create_text(400, 162, text="French", font=("Ariel", 20, "italic"))

# buttons design
right_image = PhotoImage(file='right.png')
left_image = PhotoImage(file="wrong.png")

right_button = tk.Button(window, image=right_image, text="right", bg='pink', width=100, highlightthickness=0,
                         background=BACKGROUND_COLOR, command=test)
right_button.grid(row=1, column=1)

left_button = tk.Button(image=left_image, text="left", bg='pink', width=100, highlightthickness=0,
                        background=BACKGROUND_COLOR, command=clean_text)
left_button.grid(row=1, column=0)

# DATA FRAME
data_game = pd.read_csv("french_words.csv")
data_game_dict = pd.DataFrame.to_dict(data_game, orient='records')

# new_card = random.choice(data_game_dict)
# b = data_game_dict[random.randint(0, 99)]['French']
# START PAGE

#canvas.create_text(400, 290, text="try1", tags='label1', font=("Ariel", 40, "bold"))

tk.mainloop()
