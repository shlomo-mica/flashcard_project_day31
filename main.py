import tkinter as tk
from tkinter import PhotoImage
import pandas as pd
import random
import csv
from csv import writer

d = 4
english_flip_card = {}


# TODO --After a delay of 3s (3000ms),
# the card should flip and display the English translation for the current word.
# . The card image should change to the card_back.png and the text colour should change to white.
# 2The title of the card should change to "English" from "French".
def count_down(count):
    global d
    d -= 1
    if count > 0:
        second_counter = window.after(1000, count_down, count - 1)
        print(count, 'hhh')
        timer_3second = tk.Label(text=count, background='green', font=("Ariel", 40, "bold"), width=3)
        timer_3second.grid(row=0, column=3)
        if count == 0:
            window.after_cancel(second_counter)
    else:
        english_card()


# canvas.itemconfig(timer_3second, text=f"{counter}")
def english_card():
    canvas.create_image(400, 263, image=back_photo, tags='en_card_image')
    canvas.create_text(400, 162, text="English", font=("Ariel", 20, "italic"), fill='white', tags='english_text_title')
    # canvas.itemconfig(english_text, fill='blue')
    canvas.create_text(400, 290, text=english_flip_card['English'], font=("Ariel", 40, "bold"),
                       tags='english_text_word',
                       fill='white')
    # clean_text()


def clean_text():
    canvas.delete('english_text_title')
    canvas.delete('en_card_image')
    canvas.delete('english_text_word')
    canvas.delete('label_x')

    count_down(3)
    # create texts
    card_pickup()


def card_pickup():

    global english_flip_card
    random_position = data_game_dict[random.randint(0, 99)]
    french_word = random_position['French']
    english_word = random_position['English']
    english_flip_card = random_position
    # print(english_word, french_word)
    canvas.create_text(400, 290, text=french_word, font=("Ariel", 40, "bold"), tags='label_x')
    print(f"en_flip", english_flip_card)
    return french_word, english_word


def words_to_learn_button():
    headers = ['French', 'English']
    print(f"en_flip",english_flip_card)
    row2 = [{'French': 'police', 'English': 'police'}]
    new_row = [9532, 'china', 'israel', 26]
    z=english_flip_card

    with open('maintest.csv', 'a') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        writer.writerow(z)
        # w = writer(csv_file)
        # w.writerow(row2[1])
        print(english_flip_card)



        # for h in row2.keys():
            # f.write(row2['English'])
            # f.write(row2['French'])

    print("new button")


window = tk.Tk()

# UI STAGE 1
BACKGROUND_COLOR = "#B1DDC6"
window.title("FLASH CARD GAME")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# TODO front card


canvas = tk.Canvas(window, width=800, height=526)
back_photo = tk.PhotoImage(file="card_back.png")
front_photo = tk.PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=front_photo)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
# create texts
test_text = canvas.create_text(400, 162, text="French", font=("Ariel", 20, "italic"))

# buttons design
right_image = PhotoImage(file='right.png')
left_image = PhotoImage(file="wrong.png")

right_button = tk.Button(window, image=right_image, text="right", bg='pink', width=100, highlightthickness=0,
                         background=BACKGROUND_COLOR, command=clean_text)
right_button.grid(row=1, column=1)

left_button = tk.Button(image=left_image, text="left", bg='pink', width=100, highlightthickness=0,
                        background=BACKGROUND_COLOR, command=words_to_learn_button)
left_button.grid(row=1, column=0)

# DATA FRAME


data_game = pd.read_csv("french_words.csv")
print(data_game)

data_game_dict = pd.DataFrame.to_dict(data_game, orient='records')
print(data_game_dict[6])
with open('words_to_learn.csv', 'a') as learn_file:
    learn_file.write(data_game_dict[1]['French'])
    learn_file.write(data_game_dict[1]['English'])
data_game.to_csv('test_csv', mode='a', index=False, header=False)
# pd.to_csv('test_scores.csv', mode='a', index=False, header=False)
# START PAGE

print(card_pickup())
print(f'nowwww', english_flip_card['English'])
# english_flip = card_pickup()[1]


count_down(3)
tk.mainloop()

# canvas.itemconfig(back_image)
# new_image = PhotoImage(file="new_image.png")
# old_image = PhotoImage(file="old_image.png")
# canvas_image = canvas.create_image(300, 300, image=old_image)
# #To change the image:
# canvas.itemconfig(canvas_image, image=new_image)
