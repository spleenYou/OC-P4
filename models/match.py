from random import Random
import constant.constant as CONST


class Match:
    def __init__(self, players_list, score=None):
        self.players_list = players_list
        self.score = score
        if score is None:
            self.define_color()

    def define_color(self):
        Random().shuffle(self.players_list)
        self.white_color_player = self.players_list[0]
        self.black_color_player = self.players_list[1]

    def is_finished(self):
        if self.score is not None:
            return True
        return False

    def define_score(self, winner_player):
        match winner_player:
            case CONST.NO_WINNER:
                self.score = ([self.white_color_player, 0.5], [self.black_color_player, 0.5])
            case CONST.WHITE_PLAYER:
                self.score = ([self.white_color_player, 1], [self.black_color_player, 0])
            case CONST.BLACK_PLAYER:
                self.score = ([self.white_color_player, 0], [self.black_color_player, 1])
            case _:
                pass
        self.update_players_score()

    def update_players_score(self):
        if self.score is not None:
            self.white_color_player.score = self.white_color_player.score + self.score[0][1]
            self.black_color_player.score = self.black_color_player.score + self.score[1][1]
