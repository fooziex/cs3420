class Board():
    """Store the 5x5 board data"""
    Bx=5 #x size
    By=5 #y size              # <- these should probably be constants somewhere
    Cn=4 #number to connect
    marks=list()
    for i in range(Bx):
        marks.append([0]*By)
