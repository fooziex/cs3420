constants:
* database_location = r'...'
* difficulties = {0:'Easy',1:'Normal',2:'Hard'}
* board_size_x = 5
* board_size_y = 5
* winning_sequence = 4

ai:  
* difficulty
* make_move(mode=difficulty)
* make_random_move()

board:
* board_data[board_size_x][board_size_y]
* check_winning_moves()
* check_position(x,y)

player:
* id
* name
* number_wins
* number_losses
* get_player_data(database,player_id)
* write_player_data(database,player_id)

ui: #for non grahpic ui
* display_title()
* display_mode_select()
* display_difficulty_select()
* display_winning_dialog(board,player,player2=None)
* display_losing_dialog(board,player,player2=None)
* display_player_statistics(player)
* display_input_player_data(player) #can also be used for updating player data
* display_game_board(player,player=None,board)
* draw_board(board=board)
* get_player_input(board,player)


test_harness: #this stuff should be expanded
* test_winning_positions()

* Can you read this?