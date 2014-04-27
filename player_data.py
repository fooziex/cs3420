from constants import PLAYER_DATABASE

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Unicode

engine = create_engine('sqlite:///' + PLAYER_DATABASE)
Base = declarative_base()
Base.metadata.create_all(engine)


class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, unique=True, nullable=False)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)

    def __repr__(self):
        return "<Player(id='%s', name='%s', wins='%s', losses='%s')>" % (self.id, self.name, self.wins, self.losses)


class PlayerData():
    id = None
    name = None
    wins = None
    losses = None

    def list_players(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        players = session.query(Players).all()
        player_names = set()
        for player in players:
            player_names.add(player.name)
        session.close()
        return player_names

    def load_player(self, playername):
        Session = sessionmaker(bind=engine)
        session = Session()
        player = session.query(Players).filter_by(name=playername)
        if player.count() == 1:
            player_data = player.first()
            self.id = player_data.id
            self.name = player_data.name
            self.wins = player_data.wins
            self.losses = player_data.losses
        else:
            session.close()
            raise Exception  #should be more specific
        session.close()
        return player_data

    def create_player(self, playername):
        Session = sessionmaker(bind=engine)
        session = Session()

        if session.query(Player).filter_by(name=playername).count() == 0:
            new_player = Player(name=playername)
            session.add(new_player)
            self.id = new_player.id
            self.name = new_player.name
            self.wins = new_player.wins
            self.losses = new_player.losses
            session.commit()
            session.close()
        else:
            raise Exception  #should be more specific

    def __repr__(self):
        return "<Player(id='%s', name='%s', wins='%s', losses='%s')>" % (self.id, self.name, self.wins, self.losses)
