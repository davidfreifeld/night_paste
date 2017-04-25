import cmd
import Game
import sys

class PlayGame(cmd.Cmd):
    """Command-line interface for playing CodeNames game."""
    
    game = Game.Game()

    def preloop(self):
	self.do_status('')

    def postcmd(self, stop, line):
	self.do_status(line)

    def do_status(self, line):
	self.game.print_status()	

    def do_board(self, line):
        self.game.print_board()
   
    def do_key(self, line):
	self.game.print_key()

    def do_give_clue(self, line):
	clue_list = line.split()
	self.game.give_clue(clue_list[0], int(clue_list[1]))

    def do_guess_word(self, line):
	self.game.guess_word(line)

    def do_exit(self, line):
        sys.exit(0)

if __name__ == '__main__':
    PlayGame().cmdloop()
