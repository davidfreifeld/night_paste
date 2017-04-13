#!/usr/bin/python
# -*- utf-8 -*-

import numpy as np

class Game:

    def __init__(self):
        # randomly generate some words and the key
        self.words = ['tree', 'apple', 'circus', 'pig', 'face', 'mug', 'wind', 'stick', 'basket', 'picnic', 'string',
                      'cloud', 'mouth', 'candy', 'fridge', 'table', 'iron', 'spoon', 'blender', 'math', 'computer',
                      'paper', 'rocket', 'smell', 'orange']
        self.key = []

    def get_words(self):
        return self.words

    def print_board(self):
        for i in range(5):
            row = ''
            for j in range(5):
                row += '\t\t' + self.words[i*5 + j]
            print(row + '\n')
