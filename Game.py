#!/usr/bin/python
# -*- utf-8 -*-

import numpy as np
import sys

class Game:

    key_set = np.concatenate((np.repeat('blue', 9), np.repeat('red', 8), np.repeat('neutral', 7), ['assassin']))
    player_set = ['blue', 'red']

    def __init__(self):
	
	self.init_words()
	self.init_key()
	self.init_board()
	self.init_current_player_turn()

	self.current_guess_number = 0

	self.current_clue_word  = None
	self.current_clue_number = None

    def init_words(self):
        self.words = ['tree', 'apple', 'circus', 'pig', 'face', 'mug', 'wind', 'stick', 'basket', 'picnic', 'string',
                      'cloud', 'mouth', 'candy', 'fridge', 'table', 'iron', 'spoon', 'blender', 'math', 'napkin',
                      'paper', 'rocket', 'smell', 'orange']

    def init_key(self):
	self.key = np.random.choice(Game.key_set, 25, False)
 
    def init_current_player_turn(self):
	self.current_player_turn = 0

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

    def get_current_clue_word(self):
	return self.current_clue_word

    def get_current_clue_number(self):
	return self.current_clue_number

    def get_current_guesses_remaining(self):
	return self.current_clue_number + 1 - self.current_guess_number

    def print_current_clue(self):
	print(self.current_clue_word + ", " + str(self.current_clue_number))

    def print_board(self):
	self.print_array(self.board)

    def print_array(self, my_array):
	for i in range(5):
            row = ''
            for j in range(5):
                row += '\t\t' + my_array[i*5 + j]
            print(row + '\n')

    def give_clue(self, clue_word, clue_number):
	self.current_clue_word = clue_word
	self.current_clue_number = clue_number

    def guess_word(self, board_index):

	player_color = Game.player_set[self.current_player_turn]
	guess_color = self.key[board_index]

	if guess_color == 'assassin':
	    print(player_color + " player guessed the Assassin! The game is over.")
	    sys.exit(0)

	self.board[board_index] = guess_color 

	if player_color == guess_color:
	    self.current_guess_number = self.current_guess_number + 1
	    return self.get_current_guesses_remaining() > 0
	else:
	    self.current_guess_number = self.current_clue_number + 1
	    return False
	

if __name__ == "__main__":
    my_game = Game()
    print("Game words:")
    my_game.print_words()
    print("Game key:")
    my_game.print_key()
    print("Game board:")
    my_game.print_board()
    print("After giving a clue:")
    my_game.give_clue("seed", 2)
    my_game.print_current_clue()
    print(my_game.get_current_guesses_remaining())
    print("After guessing index 4:")
    my_game.guess_word(4)
    my_game.print_board()
    guesses_remaining = my_game.get_current_guesses_remaining()
    print("Blue player has " + str(guesses_remaining) + " guesses remaining.")


