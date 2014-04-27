PLAYER_DATABASE = r'C:\home\work\c4o5x5\player_data.db'

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

WINNING_POSITIONS=set() #using a set because the winning moves are unique

#horiz WINNING_POSITIONS
#horiz wins from to column 0 to column 3 
WINNING_POSITIONS.add(((0,0),(1,0),(2,0),(3,0)))
WINNING_POSITIONS.add(((0,1),(1,1),(2,1),(3,1)))
WINNING_POSITIONS.add(((0,2),(1,2),(2,2),(3,2)))
WINNING_POSITIONS.add(((0,3),(1,3),(2,3),(3,3)))
WINNING_POSITIONS.add(((0,4),(1,4),(2,4),(3,4)))
#horiz WINNING_POSITIONS from to column 1 to column 4
WINNING_POSITIONS.add(((1,0),(2,0),(3,0),(4,0)))
WINNING_POSITIONS.add(((1,1),(2,1),(3,1),(4,1)))
WINNING_POSITIONS.add(((1,2),(2,2),(3,2),(4,2)))
WINNING_POSITIONS.add(((1,3),(2,3),(3,3),(4,3)))
WINNING_POSITIONS.add(((1,4),(2,4),(3,4),(4,4)))

#vert WINNING_POSITIONS
#vert wins from row 0 to row 3
WINNING_POSITIONS.add(((0,0),(0,1),(0,2),(0,3)))
WINNING_POSITIONS.add(((1,0),(1,1),(1,2),(1,3)))
WINNING_POSITIONS.add(((2,0),(2,1),(2,2),(2,3)))
WINNING_POSITIONS.add(((3,0),(3,1),(3,2),(3,3)))
WINNING_POSITIONS.add(((4,0),(4,1),(4,2),(4,3)))
#vert wins from row 1 to row 4
WINNING_POSITIONS.add(((0,1),(0,2),(0,3),(0,4)))
WINNING_POSITIONS.add(((1,1),(1,2),(1,3),(1,4)))
WINNING_POSITIONS.add(((2,1),(2,2),(2,3),(2,4)))
WINNING_POSITIONS.add(((3,1),(3,2),(3,3),(3,4)))
WINNING_POSITIONS.add(((4,1),(4,2),(4,3),(4,4)))

#diag WINNING_POSITIONS
#diag wins starting in column 0
WINNING_POSITIONS.add(((0,1),(1,2),(2,3),(3,4)))
WINNING_POSITIONS.add(((0,0),(1,1),(2,2),(3,3)))
#diag wins starting in column 1
WINNING_POSITIONS.add(((1,0),(2,1),(3,2),(4,3)))
WINNING_POSITIONS.add(((1,1),(2,2),(3,3),(4,4)))
#diag wins starting in column 3
WINNING_POSITIONS.add(((3,0),(2,1),(1,2),(0,3)))
WINNING_POSITIONS.add(((3,1),(2,2),(1,3),(0,4)))
#diag wins starting in column 4
WINNING_POSITIONS.add(((4,0),(3,1),(2,2),(1,3)))
WINNING_POSITIONS.add(((4,1),(3,2),(2,3),(1,4)))
