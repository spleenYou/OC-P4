from random import Random
import constant.constant as CONST


class Match:
    def __init__(self):
        self.score_table = []

    def define_score(self, winner_player):
        match winner_player:
            case CONST.NO_WINNER:
                self.define_score_table([self.white_color_player.chess_id, 0.5],
                                        [self.black_color_player.chess_id, 0.5])
            case CONST.WHITE_PLAYER:
                self.define_score_table([self.white_color_player.chess_id, 1],
                                        [self.black_color_player.chess_id, 0])
            case CONST.BLACK_PLAYER:
                self.define_score_table([self.white_color_player.chess_id, 0],
                                        [self.black_color_player.chess_id, 1])
            case _:
                pass
        return self.score_table

    def define_score_table(self, score_table):
        self.score_table = score_table

    def define_players_colors(self, players_list):
        Random().shuffle(players_list)
        self.score_table[0][0] = players_list[0]
        self.score_table[1][0] = players_list[1]

    def is_played(self):
        if self.score_table[0][1] == 0 and self.score_table[1][1] == 0:
            return False
        return True
