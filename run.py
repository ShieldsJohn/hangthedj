import random
from title import game_title
from musicians import musicians_list
musician = " "


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


def run_game():
    global tries
    list_musician = (musician_blanks())
    print(list_musician)
    guessed_letters = [] 
   
    while tries > 0:
        letter = letter_validation()

        if letter in list_musician:
            print(f"Correct - {tries} tries remaining!")
        elif letter in guessed_letters:
            print(f"You have already guessed {letter}, please try again.")
        else:
            tries -= 1
            print(f"Incorrect - {tries} tries remaining!")
        
        print(display_dj(tries))
        guessed_letters.append(letter)
        print(f"So far, you have guessed: {', '.join(guessed_letters)}")

        """
        Display correct letters replacing blanks
        """
        """
        Print next stage of hangman if incorrect
        """
        """
        End game if musician guessed or hangman stages complete
        if hangaman complete, reveal the musician
        """
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
