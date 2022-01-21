"""
Module representing the player
"""


class Player:
    """Class representing the player"""
    def __init__(self):
        self.occurring_letters = []
        self.guessed_incorrect_letters = []
        self.incorrect_count = 0
