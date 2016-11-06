class OxoBoard:
    def __init__(self,x,y):
        """ The initialiser. Initialise any fields you need here. """
        self.grid = {(0,0):0,(0,1):0,(0,2):0,(1,0):0,(2,0):0,(1,1):0,(2,2):0,(1,2):0,(2,1):0}
        self.x = x
        self.y = y
        self.gridCounter = 0


    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.grid [x,y]



    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
        If the square is not empty, leave it as-is and return False. """
        if self.grid [x,y] == 0:
            self.grid [x,y] = mark
            return True
        else:
            return False





    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        for x in xrange (0,3):
            for y in xrange(0,3):
                if self.grid[x,y] == 0:
                    return False
                else:
                    self.gridCounter += 1
        if self.gridCounter == 9:
            return True

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        if self.grid [1,1] != 0:
            if self.grid [0,0] == self.grid [1,1]:
                if self.grid [2,2] == self.grid [1,1]:
                    return True
            if self.grid [2,0] == self.grid [1,1]:
                if self.grid [0,2] == self.grid [1,1]:
                    return True
        for y in xrange(0,2):
            if self.grid [0,y] != 0:
                if self.grid[0,y] == self.grid [1,y]:
                    if self.grid[0,y] == self.grid [2,y]:
                        return True
            if self.grid [y,0] != 0:
                if self.grid [y,0] == self.grid [y,1]:
                    if self.grid [y,0] == self.grid [y,2]:
                        return True
        else:
            return False


    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


# The main game. You should not need to edit this.
if __name__ == '__main__':
    board = OxoBoard(3, 3)
    current_player = 1
    while True:
        board.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if board.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = board.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif board.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
