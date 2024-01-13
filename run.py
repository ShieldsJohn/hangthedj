import random
from title import game_title
from musicians import musicians_list
musician = ""


def musician_blanks():
    """
    Retrieves random musician name from list and replaces letters with blanks
    on the game screen
    """
    musician = random.choice(musicians_list).upper()
    return musician


def letter_validation():
    """
    Validates if a single letter has been entered
    if not, user is asked to do so.
    """
    while True:
        try:
            letter_input = input("Please enter a letter: ").upper()
            print("\n" * 3)
            if len(letter_input) == 1 and letter_input.isalpha():
                return letter_input.upper()
            else:
                print("Invalid - please enter a letter.\n")
        except ValueError:
            print("Enter one letter.\n")
    return letter_input


tries = 6


def run_game():
    """
    The main function for game processes
    """
    global tries
    musician_reveal = musician_blanks()
    list_musician = "-" * len(musician_reveal)
    guessed_letters = []
    print(list_musician)
   
    while tries > 0:
        """
        While loop executes below functions while
        tries is greater than 0
        """
        letter = letter_validation()

        if letter in guessed_letters:
            print(f"You have already guessed {letter}, please try again.")
        elif letter in musician_reveal:
            print(f"Correct - {tries} tries remaining!")
            list_musician = update_display(
                list_musician, musician_reveal, letter)
            print(list_musician)
        else:
            tries -= 1
            print(f"Incorrect - {tries} tries remaining!")
            print(list_musician)

        print(display_dj(tries))
        guessed_letters.append(letter)
        print(f"So far, you have guessed: {', '.join(guessed_letters)}")

        if list_musician == musician_reveal:
            break

    if tries == 0:
        print("YOU HANGED THE DJ!")
        print(f"The musician is - {musician_reveal}")
    else:
        print("YOU SAVED THE DJ!")
        print(f"You correctly guessed - {musician_reveal}")


def update_display(current_display, word, letter):
    """
    Update the display based on the guessed letter
    """
    new_display = ""
    for i in range(len(word)):
        if word[i] == letter:
            new_display += letter
        else:
            new_display += current_display[i]
    return new_display
    
    """
    Ask to play again
    """


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
    run_game()


main()
