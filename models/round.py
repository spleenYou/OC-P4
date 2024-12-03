from models.match import Match


class Round:
    def __init__(self):
        self.matches_list = []

    def define_matches(self):
        players_number = len(self.players_list)
        for i in range(0, players_number, 2):
            self.add_match(Match([self.players_list[i], self.players_list[i + 1]]))
        return True

    def add_match(self, match=None):
        if match is None:
            match = Match()
        self.matches_list.append(match)
        return match

    def add_players_list(self, players_list):
        self.players_list = players_list

    def is_finished(self):
        for match in self.matches_list:
            if not match.is_played():
                return False
        return True

    def make_matches(self, players_list):
        for i in range(0, len(self.matches_list)):
            self.matches_list[i].define_players_colors([players_list[i * 2], players_list[(i * 2) + 1]])
        return None
