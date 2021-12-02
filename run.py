"""
Hangman game for python terminal
"""
# Imports the word for the player to guess
import random
from words import words
# Imports the hangman diagram
from hangmen import hangmen
from player import Player

def play_game():
    """
    Start a game of hangman
    """
    random_word = random.choice(words).upper()
    word_chars = list(random_word)

    print(word_chars)

    print("Let's play the hangman game!")

    # Instantiates the player
    player = Player()

    while 1:
        letter = input('To make your guess, choose a letter from A-Z & press enter: ')

        try:
            # Checks if input has a value, if not raise exception
            if letter:
                pass
            else:
                raise ValueError('Oops, something was wrong. Try again!')

            print(letter)

            # Get all chars from the word where there is a match with occuring letters
            valid_indices = [index for index, char in enumerate(word_chars) if letter in char]

            print(valid_indices)

            # Validates the players input
            for index in valid_indices:
                # Adds the guessed letter on all occurring indices
                if index not in player.occurring_letters:
                    player.occurring_letters.append(index)
                else:
                    raise ValueError('Enter a new letter!')

            print(player.occurring_letters)

            total_list = ''
            # Validates the players char
            for index in enumerate(word_chars):
                if index in player.occurring_letters:
                    total_list += word_chars[index] + ' '
                else:
                    total_list += '_ '

            print(total_list)

            no_match = letter not in word_chars
            # When no match, add incorrect count.
            if no_match:
                print(hangmen[player.incorrect_count])
                player.incorrect_count += 1

            print(player.incorrect_count)

            # When max allowed incorrect guesses has been made, end game.
            if player.incorrect_count >= 8:
                print(f'The correct answer was {random_word}')
                break

            # When accepted chars and actual word chars is correct,
            # should probably change diff in other way.
            if len(player.occurring_letters) == len(word_chars):
                print(total_list)
                print('Congratulations, You won!')
                break

        # Catch and print error
        except ValueError as err:
            print(err)

play_game()
