from constants import WINNING_POSITIONS
import random

class AI():

    difficulty=0

    def make_random_move(self,board,player_name='CPU'):
        #makes a random move
        while board.check_winning_positions() == (False, False):
            xpos = random.randint(0,4)
            ypos = random.randint(0,4)
            if board.marks[xpos][ypos] is None:  # this, with the returns below, is like the while()
                return (xpos, ypos)
    
    def check_impending_win(self, board, player_name):
        #detects if player_name is 1 move away from winning and returns the coordinates
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
        return False, False
    
    def make_move(self, board, ai_name, human_name):
        #checks for a winning position
        win_x,win_y = self.check_impending_win(board, ai_name)
        if (win_x,win_y) != (False,False):
            return (win_x, win_y)

        if self.difficulty > 0:
            #blocks opponent from winning
            win_x,win_y = self.check_impending_win(board, human_name)
            print('Checking for impending win:')
            if (win_x, win_y) != (False,False):
                return (win_x, win_y)

        if self.difficulty > 1:
            #picks next best move
            score = self.pick_best_corner_position(board,ai_name,human_name)
            best_x,best_y = self.pick_best_spot(score)
            if (best_x, best_y) != (None,None):
                return (best_x, best_y)

        return self.make_random_move(board,ai_name)
        
    def pick_best_corner_position(self, board,this_player,other_player):
        #NorthWest Corner
        nw_corner = set( ((0,0),(1,0),(0,1),(1,1)) )

        score=list()
        for i in range(5):
            score.append([0]*5)

        for pos in nw_corner:
            x=pos[0]
            y=pos[1]
            if board.marks[x][y] != None:
                score[x][y]=0
                continue
            #check to the east
            for i in range(1,4):
                if board.marks[x][y+i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x][y+i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x][y+i] == other_player:
                    score[x][y]=score[x][y]-1
            #check to the south
            for i in range(1,4):
                if board.marks[x+i][y] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x+i][y] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x+i][y] == other_player:
                    score[x][y]=score[x][y]-1
            #check diagonally
            for i in range(1,4):
                if board.marks[x+i][y+i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x+i][y+i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x+i][y+i] == other_player:
                    score[x][y]=score[x][y]-1
            
        #Southwest Corner
        sw_corner = set( ((4,0),(3,0),(4,1),(3,1)) )

        for pos in sw_corner:
            x=pos[0]
            y=pos[1]
            if board.marks[x][y] != None:
                score[x][y]=0
                continue
            #check to the east
            for i in range(1,4):
                if board.marks[x][y+i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x][y+i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x][y+i] == other_player:
                    score[x][y]=score[x][y]-1
            #check to the north
            for i in range(1,4):
                if board.marks[x-i][y] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x-i][y] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x-i][y] == other_player:
                    score[x][y]=score[x][y]-1
            #check diagonally
            for i in range(1,4):
                if board.marks[x-i][y+i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x-i][y+i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x-i][y+i] == other_player:
                    score[x][y]=score[x][y]-1
                    
        #NorthEast Corner
        ne_corner = set( ((0,4),(0,3),(1,4),(1,3)) )

        for pos in ne_corner:
            x=pos[0]
            y=pos[1]
            if board.marks[x][y] != None:
                score[x][y]=0
                continue
            #check to the west
            for i in range(1,4):
                if board.marks[x][y-i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x][y-i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x][y-i] == other_player:
                    score[x][y]=score[x][y]-1
            #check to the south
            for i in range(1,4):
                if board.marks[x+i][y] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x+i][y] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x+i][y] == other_player:
                    score[x][y]=score[x][y]-1
            #check diagonally
            for i in range(1,4):
                if board.marks[x+i][y-i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x+i][y-i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x+i][y-i] == other_player:
                    score[x][y]=score[x][y]-1
                    
        
        #SouthEast Corner
        se_corner = set( ((4,4),(3,3),(4,3),(3,4)) )

        for pos in se_corner:
            x=pos[0]
            y=pos[1]
            if board.marks[x][y] != None:
                score[x][y]=0
                continue
            #check to the west
            for i in range(1,4):
                if board.marks[x][y-i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x][y-i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x][y-i] == other_player:
                    score[x][y]=score[x][y]-1
            #check to the north
            for i in range(1,4):
                if board.marks[x-i][y] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x-i][y] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x-i][y] == other_player:
                    score[x][y]=score[x][y]-1
            #check diagonally
            for i in range(1,4):
                if board.marks[x-i][y-i] is None:
                    score[x][y]=score[x][y]+1
                elif board.marks[x-i][y-i] == this_player:
                    score[x][y]=score[x][y]+2
                elif board.marks[x-i][y-i] == other_player:
                    score[x][y]=score[x][y]-1
            
                    
        return score
    
    def pick_best_spot(self,scoreboard):
        #receives a list argument that returns the coordinates for the highest element in the list
        max_score = 0
        max_coords = (None,None)
        
        for x in range(5):
            for y in range(5):
                if scoreboard[x][y] > max_score:
                    max_score = scoreboard[x][y]
                    max_coords = (x,y)
        
        return max_coords
    
        
