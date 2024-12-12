from models.match import Match


class Round:
    """Define and manage a round"""

    def __init__(self):
        self.matches_list = []

    def add_match(
        self, white_player, black_player, white_player_score=0, black_player_score=0
    ):
        """Add a match in matches list

        Args:
            white_player (object or str): if known it's a player object, if not, it's ""
            white_player_score (int): score of the white player
            black_player (object or str): if known it's a player object, if not, it's ""
            black_player_score (int): score of the black player

        Returns:
            match (object): a match's object
        """
        match = Match(
            white_player, white_player_score, black_player, black_player_score
        )
        self.matches_list.append(match)
        return match

    def is_finished(self):
        """Returns wether the round is finished

        Returns:
            bool: True if finished, False if not
        """
        for match in self.matches_list:
            if not match.is_played():
                return False
        return True

    def make_matches(self, players_list):
        """Initiate round's matches

        Args:
            players_list (list): Round's players list
        """
        for i in range(0, len(self.matches_list)):
            self.matches_list[i].define_players_colors(
                [players_list[i * 2], players_list[(i * 2) + 1]]
            )
