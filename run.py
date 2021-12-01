# Imports the word for the player to guess 
import random
from words import words

# Class representing the player
class Player:
    def __init__(self):
        self.occurring_letters = []

# Turns the random word into a list of characters
def play_game():
    random_word = random.choice(words).upper()
    word_chars = list(random_word)

    print(word_chars)

    print("Let's play the hangman game!")

    # Instantiates the player
    player = Player()

    while(1):
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
            for index, char in enumerate(word_chars):
                if index in player.occurring_letters:
                    total_list += word_chars[index] + ' '
                else:
                    total_list += '_ '

            print(total_list)   
        # Catch and print error
        except ValueError as err:
           print(err) 

play_game()
