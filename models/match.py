from random import Random


class Match:
    """Manage a match, can be initiate with players and scores

    Args:
        white_player (object or str): if known it's a player object, if not, it's ""
        white_player_score (int): score of the white player
        black_player (object or str): if known it's a player object, if not, it's ""
        black_player_score (int): score of the black player
    """

    def __init__(self, white_player, white_player_score, black_player, black_player_score):
        self.white_player = {"player": white_player,
                             "score": white_player_score}
        self.black_player = {"player": black_player,
                             "score": black_player_score}

    def define_score(self, winner_player):
        """Define players scores

        Args:
            winner_player (object): Player who win, None if tie game
        """
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
        self.update_scores()
        return True

    def update_scores(self):
        """Update players total scores after defining the winner
        """
        self.white_player["player"].update_score(self.white_player["score"])
        self.black_player["player"].update_score(self.black_player["score"])

    def define_players_colors(self, players_list):
        """Defining players colors randomly

        Args:
            players_list (list): List of two players
        """
        Random().shuffle(players_list)
        self.white_player["player"] = players_list[0]
        self.black_player["player"] = players_list[1]

    def is_played(self):
        """Returns whether the match is played or not

        Returns:
            bool: True if played, False if not
        """
        if (self.white_player["score"] == 0) and (self.black_player["score"] == 0):
            return False
        return True

    def have_players(self):
        """Returns whether players have been defined

        Returns:
            bool: True if players, False if not
        """
        if (self.white_player["player"] is not None) and (self.black_player["player"] is not None):
            return True
        return False
