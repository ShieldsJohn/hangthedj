import random
from title import game_title
from musicians import musicians_list


def musician_blanks():
    """
    Retrieves random musician name from list and replaces letters with blanks
    on the game screen
    """
    musician = random.choice(musicians_list).upper()
    return musician


def letter_validation():
    while True:
        try:
            letter_input = input("Please enter a letter: \n").upper()
            if len(letter_input) == 1 and letter_input.isalpha():
                return letter_input.upper()
            else:
                print("Invalid - please enter a letter.\n")
        except ValueError:
            print("Enter one letter.\n")
    return letter_input


tries = 6
guessed_letters = []
guessed = False
display = " "
musician = musician_blanks()
list_musician = list(musician)
letter_input = letter_validation()


def run_game(musician):
    for letter_input in list_musician:
        if letter_input in list_musician:
            guessed = True
            print("Well done - correct guess!")
            break
        else:
            print("This letter is not in the word - please try again!")


def display_dj(tries):
    """
    Display the hangman through its various stages to completion
    The code for this function is external, as detailed in README
    """

    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    return stages[tries]


def main():
    game_title()
    print(display_dj(tries))
    print(musician_blanks())
    letter_validation()
    run_game(musician)


main()
