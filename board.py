#       board, with coordinates
# (0,0) | (1,0) | (2,0) | (3,0) | (4,0)
# ------+-------+-------+-------+------
# (0,1) | (1,1) | (2,1) | (3,1) | (4,1)
# ------+-------+-------+-------+------
# (0,2) | (1,2) | (2,2) | (3,2) | (4,2)
# ------+-------+-------+-------+------
# (0,3) | (1,3) | (2,3) | (3,3) | (4,3)
# ------+-------+-------+-------+------
# (0,4) | (1,4) | (2,4) | (3,4) | (4,4)

winning_positions=set() #using a set because the winning moves are unique

#horiz winning_positions
#horiz wins from to column 0 to column 3 
winning_positions.add(((0,0),(1,0),(2,0),(3,0)))
winning_positions.add(((0,1),(1,1),(2,1),(3,1)))
winning_positions.add(((0,2),(1,2),(2,2),(3,2)))
winning_positions.add(((0,3),(1,3),(2,3),(3,3)))
winning_positions.add(((0,4),(1,4),(2,4),(3,4)))
#horiz winning_positions from to column 1 to column 4
winning_positions.add(((1,0),(2,0),(3,0),(4,0)))
winning_positions.add(((1,1),(2,1),(3,1),(4,1)))
winning_positions.add(((1,2),(2,2),(3,2),(4,2)))
winning_positions.add(((1,3),(2,3),(3,3),(4,3)))
winning_positions.add(((1,4),(2,4),(3,4),(4,4)))

#vert winning_positions
#vert wins from row 0 to row 3
winning_positions.add(((0,0),(0,1),(0,2),(0,3)))
winning_positions.add(((1,0),(1,1),(1,2),(1,3)))
winning_positions.add(((2,0),(2,1),(2,2),(2,3)))
winning_positions.add(((3,0),(3,1),(3,2),(3,3)))
winning_positions.add(((4,0),(4,1),(4,2),(4,3)))
#vert wins from row 1 to row 4
winning_positions.add(((0,1),(0,2),(0,3),(0,4)))
winning_positions.add(((1,1),(1,2),(1,3),(1,4)))
winning_positions.add(((2,1),(2,2),(2,3),(2,4)))
winning_positions.add(((3,1),(3,2),(3,3),(3,4)))
winning_positions.add(((4,1),(4,2),(4,3),(4,4)))

#diag winning_positions
#diag wins starting in column 0
winning_positions.add(((0,1),(1,2),(2,3),(3,4)))
winning_positions.add(((0,0),(1,1),(2,2),(3,3)))
#diag wins starting in column 1
winning_positions.add(((1,0),(2,1),(3,2),(4,3)))
winning_positions.add(((1,1),(2,2),(3,3),(4,4)))
#diag wins starting in column 3
winning_positions.add(((3,0),(2,1),(1,2),(0,3)))
winning_positions.add(((3,1),(2,2),(1,3),(0,4)))
#diag wins starting in column 4
winning_positions.add(((4,0),(3,1),(2,2),(1,3)))
winning_positions.add(((4,1),(3,2),(2,3),(1,4)))

class Board():
    """Store the 5x5 board data"""
    Bx=5 #x size
    By=5 #y size              # <- these should probably be constants somewhere
    Cn=4 #number to connect
    marks=list()
    for i in range(Bx):
        marks.append([None]*By)
    
    def check_winning_positions(marks=marks,winning_positions=winning_positions): #defaults to hard coded winning positions, and the board in this class..
        """Returns the player name/number, and the winning positions that player held, if any. Stops after finding a winning move. Returns (False, False) if no winning moves are found. Returns (player_name,winning_positions) if one is found."""
        for positions in wins:
            to_match = Board.marks[positions[0][0]][positions[0][1]] #this is the player in the first position of the winning moves
            if to_match is None:
                continue #no player has this spot, so there can't be a winner in this set of positions
            count = 0 #number of positions in a row that match
            #we now check whether all the positions are the same as "to_match"
            for position in positions:
                xpos = position[0]
                ypos = position[1]
                if Board.marks[xpos][ypos] != to_match:
                    continue
                elif Board.marks[xpos][ypos] == to_match:
                    count = count + 1
            if count == 4:
                return (to_match,positions)
        return (False,False)
