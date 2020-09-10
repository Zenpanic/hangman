# To-do list:

#   2 - Make the word_list more flexible, readable from a txt file
#   3 - Make the hangman drawing at all the steps
#   4 - Implement the coutdown function (game over when hangman full)


import re
import random
import tkinter as tk


word_list = ["cookie", "telescope", "robot", "couch", "australia", "zebra", "guitar", "python",
             "phosphorescent", "highway", "elevator", "woods", "cellar", "kangaroo", "poltergeist", "pineapple", "forbidden", "treasure", "drawer", "garbage", "truck", "ocean", "radar", "groceries", "furniture", "indigo", "moisture", "zoo", "velociraptor", "family", "mushroom", "fireplace"]


lucky_number = 0
word = ""
steps = 0
door = "_"
answer = []
mistakes = 0
used_letters = set()


def format_answer():  # Returns the answer as a nice readale string.

    global answer

    return (" ".join(answer)).upper()


def update_answer(letter):

    global answer
    global word

    for index, item in enumerate(word):
        if item == letter:
            answer[index] = word[index]

    return format_answer()


def start_game():

    if playButton["text"] == "Play":
        playButton["text"] = "Guess a letter! :"
        playButton["state"] = tk.DISABLED

    set_new_game()


def letter_used(letter):

    global used_letters

    used_letters.add(letter)
    mistakesLabel["text"] = "Used letters: " + (" ".join(used_letters)).upper()


def reset_game():

    global mistakes
    global used_letters
    global steps

    answerLabel["text"] = ""
    playButton['text'] = "Play"
    playButton["state"] = tk.NORMAL
    validInput['state'] = tk.DISABLED
    mistakesLabel["text"] = ""
    used_letters.clear()
    mistakes = 0
    steps = 0


def check_letter():

    global steps
    global answer
    global word
    global mistakes
    global used_letters

    regex = r"^[a-z]$"  # The pattern locks on a single alphabetical character.

    letter = letterInput.get()

    if re.search(regex, letter):

        if (letter in word) and not (letter in answer):
            feedbackLabel[
                "text"] = f"Well done!"
            answerLabel["text"] = update_answer(letter)

        else:
            feedbackLabel[
                "text"] = f"Bad luck! Try again."

        letter_used(letter)

    steps += 1

    letterInput.delete(0, tk.END)

    if door not in answer:
        feedbackLabel["text"] = f"Congratulations, you've guessed the word {format_answer()}. It took you 'only' {steps} guesses."
        reset_game()


def set_new_game():
    global lucky_number
    global word
    global steps
    global answer
    global door

    validInput["state"] = tk.NORMAL

    lucky_number = random.randint(0, len(word_list)-1)
    word = word_list[lucky_number]
    steps = 0

    # We put as many placeholders as there are letters in the player's guess.
    answer = [door for i in range(len(word))]

    feedbackLabel["text"] = "Make your first move!"
    answerLabel["text"] = format_answer()


window = tk.Tk()
window.geometry("700x600")
window.title("Z-Hangman")

frame1 = tk.Frame(window, width=200, height=100)
frame1.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame2 = tk.Frame(window, width=200, height=100)
frame2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame3 = tk.Frame(window, width=550, height=100)
frame3.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame4 = tk.Frame(window, width=200, height=100)
frame4.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frame5 = tk.Frame(window, width=200, height=100)
frame5.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


titleLabel = tk.Label(
    frame1,
    text=f'Welcome to the Z-Hangman!',
    fg="black")
titleLabel.pack()

playButton = tk.Button(
    frame2,
    text=f"Play",
    fg="black",
    command=start_game,
    width=25,
    height=5)
playButton.pack()

answerLabel = tk.Label(
    frame3,
    text="Wanna play a game?",
    width=100
)
answerLabel.pack()

feedbackLabel = tk.Label(
    frame3,
    text="Waiting...",
    width=200
)
feedbackLabel.pack()


letterInput = tk.Entry(frame4, width=1)
letterInput.pack()

validInput = tk.Button(
    frame4,
    text="Try",
    command=check_letter,
    state=tk.DISABLED
)
validInput.pack()

mistakesLabel = tk.Label(
    frame4,
    text="",
    width=200
)
mistakesLabel.pack()

quitButton = tk.Button(
    frame5,
    text="QUIT",
    fg="red",
    command=quit)
quitButton.pack()


window.mainloop()
