import re
import random

word_list = ["cookie", "telescope", "robot", "couch", "australia", "zebra", "guitar", "python",
             "phosphorescent", "highway", "elevator", "woods", "cellar", "kangaroo", "poltergeist"]


def format_answer(answer):

    # Returns the answer as a nice readale string.

    return "".join(answer)


def update_answer(answer, word, letter):

    # We loop through the word to know the locations of the letter, and assign the same locations in the answer.

    for index, item in enumerate(word):
        if item == letter:
            answer[index] = word[index]

    return format_answer(answer)


def prompt_guess():

    regex = r"^[a-z]$"  # The pattern locks on a single alphabetical character.

    lucky_number = random.randint(0, len(word_list))
    word = word_list[lucky_number]
    steps = 0
    door = "*"

    # We put as many placeholders as there are letters in the player's guess.
    answer = [door for i in range(len(word))]

    # It loops as long as there are placeholders in the temporary answer.
    while door in answer:
        letter = input("Guess a letter! : ")
        if re.search(regex, letter):
            if (letter in word) and not (letter in answer):
                print(
                    f"Well done! For now, you've got {update_answer(answer, word, letter)}")
            else:
                print(
                    f"Bad luck! Try again. For now, you've got {format_answer(answer)}")
        steps += 1

    print(
        f"Congratulations, you've guessed the word {word}. It took you 'only' {steps} guesses.")


prompt_guess()
