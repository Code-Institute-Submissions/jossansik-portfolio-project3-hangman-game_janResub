import random
from words import words

def play_game():
    random_word = random.choice(words).upper()
    word_chars = list(random_word)

    print(word_chars)

    print("Let's play the hangman game!")

    letter = input('To make your guess, choose a letter from A-Z & press enter: ')

    print(letter)

play_game()
