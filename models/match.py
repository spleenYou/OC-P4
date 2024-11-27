from random import Random
from constante import constante


class Match:
    def __init__(self, list_players, score=None):
        self.list_players = list_players
        self.define_color()
        self.const = constante.Constante()
        self.score = score

    def define_color(self):
        Random().shuffle(self.list_players)
        self.white_color_player = self.list_players[0]
        self.black_color_player = self.list_players[1]

    def define_score(self, winner_player):
        match winner_player:
            case self.const.NO_WINNER:
                self.score = ([self.white_color_player.chess_id, 0.5], [self.black_color_player.chess_id, 0.5])
            case self.const.WHITE_PLAYER:
                self.score = ([self.white_color_player.chess_id, 1], [self.black_color_player.chess_id, 0])
            case self.const.BLACK_PLAYER:
                self.score = ([self.white_color_player.chess_id, 0], [self.black_color_player.chess_id, 1])
            case _:
                pass
        self.update_players_score()

    def update_players_score(self):
        if self.score is not None:
            self.white_color_player.score = self.white_color_player.score + self.score[0][1]
            self.black_color_player.score = self.black_color_player.score + self.score[1][1]
