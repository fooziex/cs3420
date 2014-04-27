from constants import WINNING_POSITIONS
import random

class AI():
    def make_random_move(self, board, player_name):
        while board.check_winning_positions() == (False, False):
            xpos = random.randint(0, 4)
            ypos = random.randint(0, 4)
            if board.marks[xpos][ypos] is None:  # this, with the returns below, is like the while()
                board.marks[xpos][ypos] = player_name
                return board
        print(board.check_winning_positions()[0]+' wins with '+str(board.check_winning_positions()[1]))

    def check_impending_win(self, board, player_name):
        for winning_move in WINNING_POSITIONS:
            for i in range(4):
                almost_moves = list(winning_move)
                check_move = almost_moves[i]
                almost_moves.remove(check_move)
                count = 0
                for place in almost_moves:
                    if board.marks[place[0]][place[1]] == player_name :
                        count = count + 1
                if count == 3 :
                    if board.marks[check_move[0]][check_move[1]] is None:
                        return check_move
