#!/usr/bin/python
# -*- utf-8 -*-

import numpy as np

class Game:

    key_set = np.concatenate((np.repeat('blue', 9), np.repeat('red', 8), np.repeat('neutral', 7), ['assassin']))

    def __init__(self):
        # randomly generate some words and the key
	self.init_words()
	self.init_key()

    def init_words(self):
        self.words = ['tree', 'apple', 'circus', 'pig', 'face', 'mug', 'wind', 'stick', 'basket', 'picnic', 'string',
                      'cloud', 'mouth', 'candy', 'fridge', 'table', 'iron', 'spoon', 'blender', 'math', 'napkin',
                      'paper', 'rocket', 'smell', 'orange']

    def init_key(self):
	self.key = np.random.choice(Game.key_set, 25, False)
 
    def get_words(self):
        return self.words

    def print_words(self):
	self.print_array(self.words)

    def get_key(self):
	return self.key

    def print_key(self):
	self.print_array(self.key)

    def print_array(self, my_array):
	for i in range(5):
            row = ''
            for j in range(5):
                row += '\t\t' + my_array[i*5 + j]
            print(row + '\n')

if __name__ == "__main__":
    my_game = Game()
    print("Game words:")
    my_game.print_words()
    print("Game key:")
    my_game.print_key()
