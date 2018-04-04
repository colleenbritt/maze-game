'''
Maze Game
'''
import sys
import random
class Game:
    '''
    Game object
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.board = []

    def populate_board(self):
        '''
        Populates the board
        '''
        for i in range(0, self.width):
            self.board.append([])
            for length in range(0, self.height):
                if length == 0 or length == self.width - 1: #top and bottom row boundaries
                    self.board[i].append(" 0 ")
                elif i == 0 or i == self.height - 1: #first and last column boundaries
                    self.board[i].append(" 0 ")
                else:
                    self.board[i].append(" 1 ")

        # hard code entry and exit
        # line 23 = exit
        # line 25 = entry
        self.board[0][self.width - 2] = " 1 "
        self.board[self.height - 1][1] = " 1 "

    # hard code boundaries
    def create_boundaries(self):
        '''
        Creates the boundaries
        '''
        for bound in range(2, 6):
            self.board[2][bound] = " 0 "
        for bound in range(3, 7):
            self.board[5][bound] = " 0 "

    def print_board(self):
        '''
        Prints the board
        '''
        for line in range(0, self.width):
            #.join on space removes brackets, commas, and quotes when printing lists
            print(' '.join(self.board[line]))

    def get_height(self):
        '''
        Returns the height
        '''
        return self.height

    def get_width(self):
        '''
        Returns the width
        '''
        return self.width

    def get_board(self):
        '''
        Returns the board
        '''
        return self.board

    def set_board(self, board):
        '''
        Sets the board
        '''
        self.board = board

    def get_random_space(self, low, high):
        '''
        Returns the random space
        '''
        return random.randrange(low, high)

    # '#' character denotes enemy
    def populate_enemies(self, count):
        '''
        Populates the board with enemies
        '''
        for i in range(0, count):
            rand_width = self.get_random_space(1, self.width - 1)
            rand_height = self.get_random_space(1, self.height - 1)
            self.board[rand_height][rand_width] = " # "
#Board width and height is taken from command line arguments
#[1] is width
#[2] is height
if int(sys.argv[1]) < 5 or int(sys.argv[2]) < 5:
    print("Height and width must be 5 or higher. Exiting program")
    sys.exit()
GAME = Game(int(sys.argv[1]), int(sys.argv[2]))

GAME.populate_board()
GAME.populate_enemies(5)
GAME.create_boundaries()

#Game logic starts here.
playing = True
playerposition = GAME.get_board()
x = GAME.get_height() - 1
y = 1
playerposition[x][y] = " 2 "

GAME.set_board(playerposition)
GAME.print_board()

finish_height = 0
finish_width = GAME.get_width() - 2

def player_movement(event):
    '''
    Determines the movement of the player based on the
    user's choice of direction.
    '''
    global y
    global x
    global playing

    # if user makes it to the end
    if y == finish_width and x == finish_height:
        playing = False

    # move up
    if event == "w" or event == "W":
        if  x - 1 < GAME.get_width() and playerposition[x - 1][y] != " 0 ":
            playerposition[x][y] = " 1 "
            x -= 1
            playerposition[x][y] = " 2 "
        else:
            print("Invalid move. Try again.")
    # move down
    elif event == "s" or event == "S":
        if x + 1 < GAME.get_width() and playerposition[x + 1][y] != " 0 ":
            playerposition[x][y] = " 1 "
            x += 1
            playerposition[x][y] = " 2 "
        else:
            print("Invalid move. Try again.")
    # move right
    elif event == "d" or event == "D":
        if y + 1 < GAME.get_height() and playerposition[x][y + 1] != " 0 ":
            playerposition[x][y] = " 1 "
            y += 1
            playerposition[x][y] = " 2 "
        else:
            print("Invalid move. Try again.")
    # move left
    elif event == "a" or event == "A":
        if y - 1 < GAME.get_height() and playerposition[x][y - 1] != " 0 ":
            playerposition[x][y] = " 1 "
            y -= 1
            playerposition[x][y] = " 2 "
        else:
            print("Invalid move. Try again.")
    else:
        print("Invalid key. Use WASD only.")
# game is running here
while playing:
    player_movement(input("Move to? "))
    GAME.set_board(playerposition)
    #os.system("cls")
    GAME.print_board()
print("Congrats!")
