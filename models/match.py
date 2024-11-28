from random import Random
import constant.constant as CONST


class Match:
    def __init__(self, list_players, score=None):
        self.list_players = list_players
        self.score = score
        if score is None:
            self.define_color()

    def define_color(self):
        Random().shuffle(self.list_players)
        self.white_color_player = self.list_players[0]
        self.black_color_player = self.list_players[1]

    def define_score(self, winner_player):
        match winner_player:
            case CONST.NO_WINNER:
                self.score = ([self.white_color_player.chess_id, 0.5], [self.black_color_player.chess_id, 0.5])
            case CONST.WHITE_PLAYER:
                self.score = ([self.white_color_player.chess_id, 1], [self.black_color_player.chess_id, 0])
            case CONST.BLACK_PLAYER:
                self.score = ([self.white_color_player.chess_id, 0], [self.black_color_player.chess_id, 1])
            case _:
                pass
        self.update_players_score()

    def update_players_score(self):
        if self.score is not None:
            self.white_color_player.score = self.white_color_player.score + self.score[0][1]
            self.black_color_player.score = self.black_color_player.score + self.score[1][1]
