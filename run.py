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
Let's play a game of animal word-hangman! To restart the game, type RESTART!

Rules:
* Guess the secret word, represented by dashes for each letter of the word.
* If the guessed letter occurs in the word, it is written out in all its
correct positions.
* If the guessed letter does not occur in the word, one element of a
hanged stick figure is drawn out as a tally mark.
* After 8 incorrect guesses, the hanged man is completed and the guesser loses.
* If the word is correctly guessed, the game is over and the player wins.

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
    restart_game = False

    print(RULES)

    guess_the_word = "Guess the animal: "

    for _ in word_chars:
        guess_the_word += "_ "

    print(guess_the_word, "\n")

    # Instantiates the player
    player = Player()

    while True:
        letter = input("To make your guess, choose a " +
                       "letter from A-Z & press enter:\n")

        try:
            letter = letter.upper()
            restart_game = should_restart_game(letter)
            if (restart_game):
                break
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

    # Restarts the game based on user interaction
    if restart_game:
        play_game()

    # Lets player interact to play again
    input("Press ENTER to try again\n")
    play_game()


def should_restart_game(letter):
    """
    Lets player restart the game.
    """
    if letter == "RESTART":
        return True
    return False


def validate_input(letter):
    """
    Validates input with regular expression
    """
    if not letter:
        raise ValueError("Empty input is given, please give letter input!\n")

    is_valid_letter = re.search(r"[A-Z]", letter)

    # Checks if input has a value, if not raise exception
    if is_valid_letter and len(letter) == 1:
        pass
    else:
        raise ValueError("Input must be a letter (A-Z)!\n")


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
            raise ValueError(f"\nYou already guessed {letter}. " +
                             "Try another letter!\n")


def show_game_progress(word_chars, player):
    """
    Print out the progress for each attempt
    """
    progress = "\nGuess the animal: "
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
        if letter not in player.guessed_incorrect_letters:
            player.guessed_incorrect_letters.append(letter)
            print(hangmen[player.incorrect_count])
            player.incorrect_count += 1
        else:
            print(f"\nYou already guessed {letter}. Try another letter!\n")

    if player.guessed_incorrect_letters:
        print("\nWrong guesses:", ", ".join(player.guessed_incorrect_letters),
              "\n")


def too_many_failed_attempts(random_word, player):
    """
    When max allowed incorrect guesses has been made, end game
    """
    if player.incorrect_count >= 8:
        print(f"The correct answer was {random_word}\n")
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
