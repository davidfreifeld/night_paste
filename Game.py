#!/usr/bin/python
# -*- utf-8 -*-

import numpy as np
import sys
from nltk.corpus import words

class Game:

    ##########################
    ##  Initialize the Game ##
    ##########################
 
    key_set = np.concatenate((np.repeat('BLUE', 9), np.repeat('RED', 8), np.repeat('NEUTRAL', 7), ['ASSASSIN']))
    player_set = ['BLUE', 'RED']

    def __init__(self):
	
	self.init_words()
	self.init_key()
	self.init_board()
	self.init_current_player_turn()

	self.current_guess_number = 0

	self.current_clue_word  = None
	self.current_clue_number = None

	self.max_str_len = max(max([len(k) for k in self.key]), max([len(w) for w in self.words]))

    def init_words(self):
        # self.words = ['tree', 'apple', 'circus', 'pig', 'face', 'mug', 'wind', 'stick', 'basket', 'picnic', 'string',
        #               'cloud', 'mouth', 'candy', 'fridge', 'table', 'iron', 'spoon', 'blender', 'math', 'napkin',
        #               'paper', 'rocket', 'smell', 'orange']
	self.words = np.random.choice(words.words(), 25, False)

    def init_key(self):
	self.key = np.random.choice(Game.key_set, 25, False)
 
    def init_current_player_turn(self):
	self.current_player_turn = 0

    def init_board(self):
	self.board = list(self.words)
	

    ######################################
    ## Print/Return Info About the Game ##
    ######################################

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
	if self.current_clue_number is None:
	    return None
	return self.current_clue_number + 1 - self.current_guess_number

    def print_current_clue(self):
	print(self.current_clue_word + ", " + str(self.current_clue_number))

    def print_board(self):
	self.print_array(self.board)

    def print_array(self, my_array):
	format_string = "{0:" + str(self.max_str_len + 4) + "}"
	for i in range(5):
            row = ''
            for j in range(5):
                row += format_string.format(my_array[i*5 + j])
            print(row + '\n')
    
    def get_current_player(self):
	return Game.player_set[self.current_player_turn]

    def print_status(self):
	current_player = self.get_current_player()
	print ""
	if self.current_clue_word is None and self.current_clue_number is None:
	    print current_player + "'s turn to give a clue."
	else: 
	    print current_player + "'s turn to guess."
	    print "Clue: " + self.current_clue_word + " " + str(self.current_clue_number)
	    print str(self.get_current_guesses_remaining()) + " guesses remaining."

    #####################
    ## Act on the game ##
    #####################


    def give_clue(self, clue_word, clue_number):
	
	if self.current_clue_word is not None or self.current_clue_number is not None:
	    print self.get_current_player() + " player is not finished guessing!"
	    return False

	self.current_clue_word = clue_word
	self.current_clue_number = clue_number
	return True


    def guess_word(self, guess):

	if self.current_clue_word is None or self.current_clue_number is None:
	    print "No clue has been given yet!"
	    return False

	if guess not in self.board:
	    print guess + " is not a word on the current board!"
	    return False

	board_index = self.board.index(guess)

	player_color = self.get_current_player()
	guess_color = self.key[board_index]
	
	if guess_color == 'ASSASSIN':
	    print player_color + " player guessed the Assassin! The game is over."
	    sys.exit(0)

	self.board[board_index] = guess_color 
	self.current_guess_number = self.current_guess_number + 1

	if player_color == guess_color:
	    if self.get_current_guesses_remaining() == 0:
		self.end_turn()

	else:
	    self.end_turn()

	return True


    def end_turn(self):
	
	if self.current_clue_word is None or self.current_clue_number is None:
	    print self.get_current_player() + " player has not given a clue yet!"
	    return False

	if self.current_guess_number == 0:
	    print self.get_current_player() + " player must guess at least one word!"
	    return False	

	self.current_clue_word = None
	self.current_clue_number = None
	self.current_player_turn = (self.current_player_turn + 1) % 2
	self.current_guess_number = 0


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
    print(str(guesses_remaining) + " guesses remaining.")


