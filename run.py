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

     # Get all chars from the word where there is a match with occuring letters
    valid_indices = [index for index, char in enumerate(word_chars) if letter in char]

    print(valid_indices)

    user = User()

     # Validates the players input
    for index in valid_indices:
        # Adds the guessed letter on all occurring indices
        if index not in user.occurring_letters:
            user.occurring_letters.append(index)

    print(user.occurring_letters)

play_game()
