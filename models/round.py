from models.match import Match


class Round:
    def __init__(self, players_list=[], matches_list=[]):
        self.matches_list = matches_list
        self.players_list = players_list

    def define_matches(self):
        players_number = len(self.players_list)
        for i in range(0, players_number, 2):
            self.add_match(Match([self.players_list[i], self.players_list[i + 1]]))
        return True

    def add_match(self, match):
        self.matches_list.append(match)

    def is_finished(self):
        for match in self.matches_list:
            if isinstance(match, Match):
                if not match.isfinished():
                    return False
                return True
            return False
