import random
from words import words

class User:
    def __init__(self):
        self.occurring_letters = []

def play_game():
    random_word = random.choice(words).upper()
    word_chars = list(random_word)

    print(word_chars)

    print("Let's play the hangman game!")

    letter = input('To make your guess, choose a letter from A-Z & press enter: ')

    print(letter)

     # Get all chars from actual word where we have a match.
    valid_indices = [index for index, char in enumerate(word_chars) if letter in char]
    
    print(valid_indices)

play_game()
