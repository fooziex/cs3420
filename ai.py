class AI:
    def make_random_move(board,player_name='CPU'):
        while True: #faking a do while
            xpos = random.randint(5)
            ypos = random.randint(5)
            if board.marks[xpos][ypos] == None: #this, with the break below, is like the while()
                board.marks[xpos][ypos] = player_name
                break
