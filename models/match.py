from random import Random


class Match:
    def __init__(self, list_players):
        self.list_players = list_players
        self.define_color()

    def define_color(self):
        Random().shuffle(self.list_players)
        self.white_color_player = self.list_players[0]
        self.black_color_player = self.list_players[1]

    def define_score(self, winner_player):
        match winner_player:
            case None:
                self.score = ({self.white_color_player: 0.5}, {self.black_color_player: 0.5})
            case self.white_color_player:
                self.score = ({self.white_color_player: 1}, {self.black_color_player: 0})
            case self.black_color_player:
                self.score = ({self.white_color_player: 0}, {self.black_color_player: 1})
            case _:
                self.score = None
        return self.score
