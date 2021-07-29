from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

words_dict = data.to_dict(orient="records")

french = "French"
english = "English"
word_dict = None
word_fr = None
word_en = None


# ---------------------------- Words Creation ------------------------------- #
def words_known():
    global word_dict, words_dict
    words_dict.remove(word_dict)
    df = pandas.DataFrame(words_dict)
    df.to_csv("data/words_to_learn.csv", index= False)
    random_words()


def words_unknown():
    random_words()


def display_words(word, meaning, fill_color):
    # try:
    canvas.delete("text", "text1")
    # except:
    #     pass
    # finally:
    canvas.create_text(400, 150, text=word, fill=fill_color, font=(FONT_NAME, 40, "italic"), tag="text1")
    canvas.create_text(400, 263, text=meaning, fill=fill_color, font=(FONT_NAME, 60, "bold"), tag="text")


def random_words():
    global word_dict, word_en, word_fr, timer
    window.after_cancel(timer)
    word_dict = random.choice(words_dict)
    word_fr = word_dict["French"]
    word_en = word_dict["English"]
    # window.after_cancel()
    canvas.itemconfig(canvas_image, image=card_front)
    display_words(french, word_fr, "black")

    timer = window.after(3000, func=back_flip)


def back_flip():
    canvas.itemconfig(canvas_image, image=card_back)
    display_words(english, word_en, "white")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
img_right = PhotoImage(file="images/right.png")
button_right = Button(image=img_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=words_known)
button_right.grid(row=1, column=1)

img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=img_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=words_unknown)
button_wrong.grid(row=1, column=0)
timer = window.after(3000, func=back_flip)
random_words()

# Words


# Create Word Dictionary


window.mainloop()
