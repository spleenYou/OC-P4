from random import Random


class Match:
    def __init__(self, white_player, white_player_score, black_player, black_player_score):
        self.white_player = {"player": white_player, "score": white_player_score}
        self.black_player = {"player": black_player, "score": black_player_score}

    def define_score(self, winner_player):
        match winner_player:
            case self.white_player:
                self.white_player["score"] = 1
            case self.black_player:
                self.black_player["score"] = 1
            case None:
                self.white_player["score"] = 0.5
                self.black_player["score"] = 0.5
            case _:
                pass
        self.update_score()
        return True

    def update_score(self):
        self.white_player["player"].score = self.white_player["player"].score + self.white_player["score"]
        self.black_player["player"].score = self.black_player["player"].score + self.black_player["score"]
        return True

    def define_players_colors(self, players_list):
        Random().shuffle(players_list)
        self.white_player["player"] = players_list[0]
        self.black_player["player"] = players_list[1]
        return True

    def is_played(self):
        if (self.white_player["score"] == 0) and (self.black_player["score"] == 0):
            return False
        return True

    def have_players(self):
        if (self.white_player["player"] is not None) and (self.black_player["player"] is not None):
            return True
        return False

    def get_score(self):
        return (self.white_player, self.black_player)
