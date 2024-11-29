from random import Random
from models.match import Match


class Round:
    def __init__(self, round_number, players_list, matches_list):
        self.players_list = players_list
        self.round_number = round_number
        self.matches_list = []
        if matches_list:
            self.matches_list = matches_list
        else:
            for i in range(len(players_list)):
                self.matches_list.append(())

    def define_matches(self):
        matches_list = []
        self.sort_list()
        players_number = len(self.players_list)
        for i in range(0, players_number, 2):
            matches_list.append(Match([self.players_list[i], self.players_list[i + 1]]))
        return matches_list

    def sort_list(self):
        if self.round_number == 1:
            Random().shuffle(self.players_list)
        else:
            self.players_list = sorted(self.players_list, key=lambda player: player.score, reverse=True)
            self.check_previous_meeting()

    def all_matches_finished(self):
        for match in self.matches_list:
            return False
