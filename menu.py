from player_data import PlayerData

from guidata.dataset.datatypes import DataSet, BeginGroup, EndGroup
from guidata.dataset.dataitems import ButtonItem, ChoiceItem, TextItem, StringItem





class MainMenu():
    import guidata
    _app = guidata.qapplication()

    player = PlayerData()
    players = list(player.list_players())+['New Player']
    players.sort()
    players_no_guest = list(player.list_players().difference(set(['Guest'])))
    players_no_guest.sort()


    def warn_duplicate_players(self):
        class WarnDuplicatePlayers(DataSet):
            """C4o5x5"""
            warning = StringItem('Warning', 'Please choose two different player names.')
        wdp=WarnDuplicatePlayers()
        wdp.view()

    def warn_new_player(self):
        class WarnNewPlayer(DataSet):
            """C4o5x5"""
            warning = StringItem('Warning', 'Please choose a unique player name.')
        wnp=WarnNewPlayer()
        wnp.view()

    def warn_no_humans(self):
        class WarnNoHumans(DataSet):
            """C4o5x5"""
            warning = StringItem('Warning', 'Please choose at least one human player.')
        wnh=WarnNoHumans()
        wnh.view()

    def init_menu(self):
        history_menuitem = lambda mainmenu,b,c,d: self.show_player_history(self.player.load_player(self.players_no_guest[mainmenu.player_history]))

        class MenuItems(DataSet):
            """C4o5x5"""
            player_history = ChoiceItem("Play record for:", self.players_no_guest)
            history = ButtonItem('Display', history_menuitem).set_pos(col=1)
            player_one = ChoiceItem("Player 1", self.players)
            player_two = ChoiceItem("Player 2", self.players)

        return MenuItems

    def show_menu(self):
        MenuItems = self.init_menu()
        #_app = self._app
        menu = MenuItems()
        player_one = None
        player_two = None
        exit_value = None
        while exit_value != 1:
            exit_value = menu.edit()
            player_one = menu.player_one
            player_two = menu.player_two
            if self.players[player_one] == self.players[player_two] and exit_value != 0 \
                    and self.players[player_one] != 'Guest' and self.players[player_two] != 'Guest' and self.players[player_one] != 'New Player' and self.players[player_two] != 'New Player':
                self.warn_duplicate_players()
                continue
            elif exit_value == 0:
                raise Exception
            else:
                break
        return [self.players[menu.player_one], self.players[menu.player_two]]


    def init_player_history(self, this_player):
        class PlayerHistoryItems(DataSet):
            """C4o5x5"""
            player_one_group_begin = BeginGroup(this_player.name)
            player_one_wins = StringItem('Wins', this_player.wins)
            player_one_losses = StringItem('Losses', this_player.losses)
            player_one_group_end = EndGroup(this_player.name)

        return PlayerHistoryItems

    def show_player_history(self, this_player):
        PlayerHistoryItems = self.init_player_history(this_player)
        history = PlayerHistoryItems()
        history.view()

    def init_register_player(self, player_number=None):
        class PlayerRegisterItems(DataSet):
            """c4o5x5"""
            if player_number is not None:
                player_name = StringItem('Player '+str(player_number)+' Name')
            else:
                player_name = StringItem('Name')
        return PlayerRegisterItems

    def show_register_player(self,player_number=None):
        PlayerRegisterItems = self.init_register_player(player_number)
        accept = 0
        register = PlayerRegisterItems()
        while accept == 0:
            accept = register.edit()
        new_player=register.player_name
        return new_player
