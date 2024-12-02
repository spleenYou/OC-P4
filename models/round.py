from random import Random
from models.match import Match


class Round:
    def __init__(self, players_list, matches_list=[]):
        self.players_list = players_list
        self.match = Match()
        if matches_list == []:
            self.matches_list = matches_list
        else:
            self.matches_list = self.define_matches()

    def define_matches(self):
        matches_list = []
        self.sort_list()
        players_number = len(self.players_list)
        for i in range(0, players_number, 2):
            matches_list.append(self.match([self.players_list[i], self.players_list[i + 1]]))
        return matches_list

    def sort_list(self):
        if self.round_number == 1:
            Random().shuffle(self.players_list)
        else:
            self.players_list = sorted(self.players_list, key=lambda player: player.score, reverse=True)
            self.check_previous_meeting()

    def is_finished(self):
        for match in self.matches_list:
            if not self.match.is_finished():
                return False
        return True
