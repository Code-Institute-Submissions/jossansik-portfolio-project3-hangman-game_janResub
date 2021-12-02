"""
Hangman game for python terminal
"""
# Imports the word for the player to guess
import random
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
* If the player suggest a letter which occurs in the word, it is written out in all 
its correct positions. 
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

    guess_the_word = "Guess the animal = "

    for _ in word_chars:
        guess_the_word += "_ "

    print("\n", guess_the_word, "\n")

    # Instantiates the player
    player = Player()

    while 1:
        letter = input("To make your guess, choose a letter from A-Z & press enter: ")

        try:
            # Checks if input has a value, if not raise exception
            if letter:
                pass
            else:
                raise ValueError("Oops, something was wrong. Try again!")

            # Get all chars from the word where there is a match with occuring letters
            valid_indices = [index for index, char in enumerate(word_chars) if letter in char]

            # Validates the players input
            for index in valid_indices:
                # Adds the guessed letter on all occurring indices
                if index not in player.occurring_letters:
                    player.occurring_letters.append(index)
                else:
                    raise ValueError("Enter a new letter!")

            progress = ""
            # Validates the players char
            for index, _ in enumerate(word_chars):
                if index in player.occurring_letters:
                    progress += word_chars[index] + " "
                else:
                    progress += "_ "

            print(progress)

            no_match = letter not in word_chars
            # When no match, add incorrect count.
            if no_match:
                print(hangmen[player.incorrect_count])
                player.incorrect_count += 1

            # When max allowed incorrect guesses has been made, end game.
            if player.incorrect_count >= 8:
                print(f"The correct answer was {random_word}")
                break

            # When accepted chars and actual word chars is correct,
            # should probably change diff in other way.
            if player.occurring_letters == [index for index, _ in enumerate(word_chars)]:
                print(progress)
                print("Congratulations, You won!")
                break

        # Catch and print error
        except ValueError as err:
            print(err)

play_game()
