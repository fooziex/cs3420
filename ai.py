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
