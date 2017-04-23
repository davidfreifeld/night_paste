import cmd
import Game


class PlayGame(cmd.Cmd):
    """Command-line interface for playing CodeNames game."""
    
    game = Game.Game()

    def do_print_board(self, line):
        self.game.print_board()
   
    def do_print_key(self, line):
	self.game.print_key()
 
    def do_exit(self, line):
        return True

if __name__ == '__main__':
    PlayGame().cmdloop()
