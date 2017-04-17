#!/usr/bin/python
# -*- utf-8 -*-

import numpy as np
import sys

class Game:

    key_set = np.concatenate((np.repeat('blue', 9), np.repeat('red', 8), np.repeat('neutral', 7), ['assassin']))
    player_set = ['blue', 'red']

    def __init__(self):
        # randomly generate some words and the key
	self.init_words()
	self.init_key()
	self.init_board()

    def init_words(self):
        self.words = ['tree', 'apple', 'circus', 'pig', 'face', 'mug', 'wind', 'stick', 'basket', 'picnic', 'string',
                      'cloud', 'mouth', 'candy', 'fridge', 'table', 'iron', 'spoon', 'blender', 'math', 'napkin',
                      'paper', 'rocket', 'smell', 'orange']

    def init_key(self):
	self.key = np.random.choice(Game.key_set, 25, False)
 
    def init_board(self):
	self.board = list(self.words)

    def get_words(self):
        return self.words

    def print_words(self):
	self.print_array(self.words)

    def get_key(self):
	return self.key

    def print_key(self):
	self.print_array(self.key)

    def get_board(self):
	return self.board

    def print_board(self):
	self.print_array(self.board)

    def print_array(self, my_array):
	for i in range(5):
            row = ''
            for j in range(5):
                row += '\t\t' + my_array[i*5 + j]
            print(row + '\n')

    def guess_word(self, board_index, player_index, guess_number, clue_number):

	player_color = Game.player_set[player_index]
	guess_color = self.key[board_index]

	if guess_color == 'assassin':
	    print(player_color + " player guessed the Assassin! The game is over.")
	    sys.exit(0)

	self.board[board_index] = guess_color 

	if player_color == guess_color:
	    return clue_number + 1 - guess_number

	else:
	    return 0 
	

if __name__ == "__main__":
    my_game = Game()
    print("Game words:")
    my_game.print_words()
    print("Game key:")
    my_game.print_key()
    print("Game board:")
    my_game.print_board()
    print("After guessing index 4:")
    guesses_remaining = my_game.guess_word(4, 0, 1, 2)
    my_game.print_board()
    print("Blue player has " + str(guesses_remaining) + " guesses remaining.")


