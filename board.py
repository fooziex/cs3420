from constants import WINNING_POSITIONS, BOARD_DIMENSIONS, POSITIONS_TO_WIN

class Board():
    """Store the 5x5 board data"""
    Bx = BOARD_DIMENSIONS['x']  # x size
    By = BOARD_DIMENSIONS['y']  # y size              # <- these should probably be constants somewhere
    Cn = POSITIONS_TO_WIN  # number to connect
    winning_positions=WINNING_POSITIONS
    marks = list()
    for i in range(Bx):
            marks.append([None]*By)

    def clear(self):
        self.marks = list()
        for i in range(self.Bx):
            self.marks.append([None]*self.By)

    def check_winning_positions(self):
        """Returns (False, False) if no winning moves are found or (player_name,winning_positions) if one is found."""

        for positions in self.winning_positions:
            to_match = Board.marks[positions[0][0]][positions[0][1]] # this is the player in the first position of the winning moves
            if to_match is None:
                continue  # no player has this spot, so there can't be a winner in this set of positions
            count = 0  # number of positions in a row that match
            # we now check whether all the positions are the same as "to_match"
            for position in positions:
                xpos = position[0]
                ypos = position[1]
                if Board.marks[xpos][ypos] != to_match:
                    continue
                elif Board.marks[xpos][ypos] == to_match:
                    count = count + 1
            if count == WINNING_POSITIONS:
                return to_match, positions
        return False, False

    def __repr__(self):
        return str(self.marks[0])+'\n'+str(self.marks[1])+'\n'+str(self.marks[2])+'\n'+str(self.marks[3])+'\n'+str(self.marks[4])
