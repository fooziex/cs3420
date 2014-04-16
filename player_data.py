import sqlite3 as sl
from constants import PLAYER_DATABASE

class Player_Data():
    name = None
    wins = None
    losses = None

    def load_player(self,playername):
        conn = sl.connect(PLAYER_DATABASE)
        c = conn.cursor()
        playername_sql = (playername,)
        c.execute('SELECT * FROM players WHERE name=?', playername_sql)
        if c.arraysize == 1:
            player = c.fetchone()
            self.name = player[1]
            self.wins = player[2]
            self.losses = player[3]
        else:
            raise Exception #should be more specific
        return player


    def create_player(self,playername):
        pass