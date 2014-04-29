from player_data import PlayerData

from guidata.dataset.datatypes import DataSet, BeginGroup, EndGroup
from guidata.dataset.dataitems import ButtonItem, ChoiceItem, TextItem


player = PlayerData()
players = list(player.list_players())
players.sort()


class MainMenu():
    import guidata
    _app = guidata.qapplication()

    def warn_duplicate_players(self, player_one=None, player_two=None):
        class WarnDuplicatePlayers(DataSet):
            """C4o5x5"""
            warning = TextItem('Warning', 'Please choose two different player names.')
        wdp=WarnDuplicatePlayers()
        wdp.view()

    def init_menu(self):
        exit_menuitem = lambda a, b, c, d: exit()
        history_menuitem = lambda a, b, c, d: self.show_player_history(player.load_player(players[a.player_one]),
                                                                       player.load_player(players[a.player_two]))

        class MenuItems(DataSet):
            """C4o5x5"""
            register = ButtonItem('Register', exit_menuitem)
            history = ButtonItem('History', history_menuitem)
            player_one = ChoiceItem("Player 1", players)
            player_two = ChoiceItem("Player 2", players)
            first = ChoiceItem("Who Goes First?", ("Player 1", "Player 2"))

        return MenuItems

    def show_menu(self):
        MenuItems = self.init_menu()
        #_app = self._app
        menu = MenuItems()
        player_one = None
        player_two = None
        exit_value = None
        while player_one == player_two and exit_value != 0:
            exit_value = menu.edit()
            player_one = menu.player_one
            player_two = menu.player_two
            if player_one == player_two and exit_value != 0:
                self.warn_duplicate_players()
        return menu.player_one, menu.player_two

    def init_player_history(self, player_one, player_two):
        class PlayerHistoryItems(DataSet):
            """C4o5x5"""
            player_one_group_begin = BeginGroup(player_one.name)
            player_one_wins = TextItem('Wins', player_one.wins)
            player_one_losses = TextItem('Losses', player_one.losses)
            player_one_group_end = EndGroup(player_one.name)

            player_two_group_begin = BeginGroup(player_two.name)
            player_two_wins = TextItem('Wins', player_two.wins)
            player_two_losses = TextItem('Losses', player_two.losses)
            player_two_group_end = EndGroup(player_two.name)

        return PlayerHistoryItems

    def show_player_history(self, a, b):
        PlayerHistoryItems = self.init_player_history(a, b)
        history = PlayerHistoryItems()
        history.view()
