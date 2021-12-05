"""
Hangman game for python terminal
"""
# Imports the word for the player to guess
import random
import re
from words import words
# Imports the hangman diagram
from hangmen import hangmen
from player import Player

RULES = '''
===============================================================================
Let's play a game of animal word-hangman!

Rules:
* The player will guess what animal is hidden in the secret word, which is
represented by a row of dashes for each letter of the word.
* If the player suggest a letter which occurs in the word,
it is written out in all its correct positions.
* If the suggested letter does not occur in the word, one element of a
hanged stick figure is drawn out as a tally mark.
* If the player makes 8 incorrect guesses, the hanged man diagram is completes
and the guesser loses.
* If the word is correctly guessed, the game is over and the player wins.

Press enter to start the game!

{o,o}
|)__)    Good Luck!
-“-“-

===============================================================================
'''


def play_game():
    """
    Start a game of hangman
    """
    random_word = random.choice(words).upper()
    word_chars = list(random_word)

    print(RULES)

    guess_the_word = "Guess the animal: "

    for _ in word_chars:
        guess_the_word += "_ "

    print("\n", guess_the_word, "\n")

    # Instantiates the player
    player = Player()

    while True:
        letter = input("To make your guess, choose a " +
                       "letter from A-Z & press enter: ")

        try:
            letter = letter.upper()
            validate_input(letter)
            add_letter(word_chars, player, letter)
            show_game_progress(word_chars, player)
            increase_invalid_attempts(word_chars, letter, player)
            if too_many_failed_attempts(random_word, player):
                break
            if game_won(player, word_chars):
                break
        # Catch and print error
        except ValueError as err:
            print(err)


def validate_input(letter):
    """
    Validates input with regular expression
    """
    is_valid_letter = re.search(r"[A-Z]", letter)

    # Checks if input has a value, if not raise exception
    if is_valid_letter:
        pass
    else:
        raise ValueError("Oops, you must enter a letter. Try again!")


def add_letter(word_chars, player, letter):
    """
    Adds the guessed letter to all occurring indices
    if the letter is in the word
    """
    # Get all chars from the word where there is a match with occuring letters
    valid_indices = [index for index, char in enumerate(word_chars)
                     if letter in char]

    for index in valid_indices:
        # Adds the guessed letter on all occurring indices
        if index not in player.occurring_letters:
            player.occurring_letters.append(index)
        else:
            raise ValueError("Enter a new letter!")


def show_game_progress(word_chars, player):
    """
    Print out the progress for each attempt
    """
    progress = ""
    for index, _ in enumerate(word_chars):
        if index in player.occurring_letters:
            progress += word_chars[index] + " "
        else:
            progress += "_ "

    print(progress)


def increase_invalid_attempts(word_chars, letter, player):
    """
    When no match, add incorrect count and show hangman progress
    """
    no_match = letter not in word_chars
    if no_match:
        print(hangmen[player.incorrect_count])
        player.incorrect_count += 1


def too_many_failed_attempts(random_word, player):
    """
    When max allowed incorrect guesses has been made, end game
    """
    if player.incorrect_count >= 8:
        print(f"The correct answer was {random_word}")
        return True
    return False


def game_won(player, word_chars):
    """
    When accepted chars and actual word chars is correct,
    should probably change diff in other way.
    """
    if len(player.occurring_letters) == len(word_chars):
        print("\nCongratulations, You won!\n")
        return True
    return False


play_game()
