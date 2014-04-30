from constants import HOME_DIRECTORY

import sys, os, random

os.environ["PYSDL2_DLL_PATH"] = HOME_DIRECTORY

try:
    from sdl2 import *
    import sdl2.ext as sdl2ext
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)

from sdl2.ext import Resources



class GameBoard():

    RESOURCES = Resources(HOME_DIRECTORY, "graphics")
    factory = sdl2ext.SpriteFactory(sdl2ext.SOFTWARE)

    def game_board(self, board, player_one, player_two, player_types, ai_difficulty=None):

        from player_data import PlayerData

        pd=PlayerData()

        if 'AI' in player_types:
            from ai import AI
            ai=AI()
            if 'AI: Easy' in [player_one,player_two]:
                ai.difficulty=0
            elif 'AI: Medium' in [player_one,player_two]:
                ai.difficulty=1
            elif 'AI: Hard' in [player_one,player_two]:
                ai.difficulty=2

        sdl2ext.init()

        window = sdl2ext.Window("c4o5x5", size=(320, 420))

        window.show()

        factory = sdl2ext.SpriteFactory(sdl2ext.SOFTWARE)

        spriterenderer = factory.create_sprite_render_system(window)

        moves = 0
        running = True
        updated_p1 = False
        updated_p2 = False

        while running:
            if moves % 2 == 0:
                this_player = player_one
                that_player = player_two
                if player_types[0]=='AI':
                    mode='AI'
                    player_graphic="ai.bmp"
                else:
                    mode='Human'
                    player_graphic = "player_one.bmp"
            if moves % 2 == 1:
                this_player = player_two
                that_player = player_one
                if player_types[1]=='AI':
                    mode='AI'
                    player_graphic="ai.bmp"
                else:
                    mode='Human'
                    player_graphic = "player_two.bmp"
            for x in range(5):
                for y in range(5):
                    if board.marks[x][y] is None:
                        spriterenderer.render(factory.from_image(self.RESOURCES.get_path("tile.bmp")),x*64,y*64)
                    if board.marks[x][y] == player_one:
                        spriterenderer.render(factory.from_image(self.RESOURCES.get_path("tile_o.bmp")),x*64,y*64)
                    if board.marks[x][y] == player_two:
                        spriterenderer.render(factory.from_image(self.RESOURCES.get_path("tile_x.bmp")),x*64,y*64)
            if board.check_winning_positions() != (False,False):
                winning_player = board.check_winning_positions()[0]
                if winning_player == player_one:
                    winning_graphic = 'player_one_wins.bmp'
                    if player_one != 'Guest' and not updated_p1:
                        player=pd.load_player(player_one)
                        pd.update_player(player_one,player.wins+1,player.losses)
                        updated_p1 = True
                    if player_two != 'Guest' and not updated_p2:
                        player=pd.load_player(player_two)
                        pd.update_player(player_two,player.wins,player.losses+1)
                        updated_p2=True
                elif winning_player == player_two:
                    winning_graphic = 'player_two_wins.bmp'
                    if player_one != 'Guest' and not updated_p2:
                        player=pd.load_player(player_two)
                        pd.update_player(player_two,player.wins+1,player.losses)
                        updated_p2=True
                    if player_two != 'Guest' and not updated_p1:
                        player=pd.load_player(player_one)
                        pd.update_player(player_one,player.wins,player.losses+1)
                        updated_p1=True
                spriterenderer.render(factory.from_image(self.RESOURCES.get_path(winning_graphic)),0,(x+1)*64)
                events = sdl2ext.get_events()
                for event in events:
                    if event.type == SDL_MOUSEBUTTONDOWN:
                        running = False
                        SDL_Delay(1000)
                        break
            elif moves == 25:
                winning_graphic = "tie_game.bmp"
                spriterenderer.render(factory.from_image(self.RESOURCES.get_path(winning_graphic)),0,(x+1)*64)
                events = sdl2ext.get_events()
                for event in events:
                    if event.type == SDL_MOUSEBUTTONDOWN:
                        running = False
                        break
            elif mode == 'Human':
                spriterenderer.render(factory.from_image(self.RESOURCES.get_path(player_graphic)),0,(x+1)*64)
                events = sdl2ext.get_events()
                for event in events:
                    if event.type == SDL_QUIT:
                        running = False
                        break
                    elif event.type == SDL_MOUSEBUTTONDOWN:
                        x_pos = int(event.button.x/64)
                        y_pos = int(event.button.y/64)
                        if x_pos <= 4 and y_pos <= 4 and board.marks[x_pos][y_pos] is None:
                            board.marks[x_pos][y_pos]=this_player
                            moves = moves + 1
            elif mode=='AI':
                move = ai.make_move(board,this_player,that_player)
                moves = moves + 1
                board.update_position(move[0],move[1],this_player)
                for x in range(5):
                    for y in range(5):
                        if board.marks[x][y] is None:
                            spriterenderer.render(factory.from_image(self.RESOURCES.get_path("tile.bmp")),x*64,y*64)
                        if board.marks[x][y] == player_one:
                            spriterenderer.render(factory.from_image(self.RESOURCES.get_path("tile_o.bmp")),x*64,y*64)
                        if board.marks[x][y] == player_two:
                            spriterenderer.render(factory.from_image(self.RESOURCES.get_path("tile_x.bmp")),x*64,y*64)
                spriterenderer.render(factory.from_image(self.RESOURCES.get_path(player_graphic)),0,(x+1)*64)
                SDL_Delay(500)
                events = sdl2ext.get_events()
                for event in events:
                    if event.type == SDL_QUIT:
                        running = False
                        break
                    else:
                        pass
            else:
                raise Exception
            SDL_Delay(10)

        sdl2ext.quit()
