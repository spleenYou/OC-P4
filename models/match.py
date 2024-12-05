from random import Random
import constant.constant as CONST


class Match:
    def __init__(self):
        self.score_table = []

    def define_score(self, winner_player):
        match winner_player:
            case CONST.NO_WINNER:
                self.score_table[0][1] = 0.5
                self.score_table[1][1] = 0.5
            case CONST.WHITE_PLAYER:
                self.score_table[0][1] = 1
                self.score_table[1][1] = 0
            case CONST.BLACK_PLAYER:
                self.score_table[0][1] = 0
                self.score_table[1][1] = 1
            case _:
                pass
        self.update_score()
        return True

    def update_score(self):
        self.score_table[0][0].score = self.score_table[0][0].score + self.score_table[0][1]
        self.score_table[1][0].score = self.score_table[1][0].score + self.score_table[1][1]
        return True

    def define_score_table(self, score_table):
        self.score_table = score_table
        return True

    def define_players_colors(self, players_list):
        Random().shuffle(players_list)
        self.score_table[0][0] = players_list[0]
        self.score_table[1][0] = players_list[1]
        return True

    def is_played(self):
        if self.score_table[0][1] == 0 and self.score_table[1][1] == 0:
            return False
        return True
