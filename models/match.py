import constant.constant as CONST


class Match:
    def __init__(self, score_table):
        self.score_table = score_table

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
