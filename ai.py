import random

class AI():
    def make_random_move(self,board,player_name='CPU'):
        while True: #faking a do while
            xpos = random.randint(0,4)
            ypos = random.randint(0,4)
            if board.marks[xpos][ypos] == None: #this, with the returns below, is like the while()
                board.marks[xpos][ypos] = player_name
                return board
        #There's a bug in make_random_move somewhere. It's probably to do with how Python deals with classes; I get an error when I try to pass the board object to this function. I'll fix it unless someone else figures it out.
