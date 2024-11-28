from random import Random
from models.match import Match


class Round:
    def __init__(self, round_number, players_list, previous_matches_list):
        self.players_list = players_list
        self.round_number = round_number
        self.previous_matches_list = previous_matches_list

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

    def check_previous_meeting(self):
        list_to_checked = self.players_list
        checked_list = [list_to_checked[0]]
        del list_to_checked[0]
        for player in self.players_list:
            for round in self.previous_matches_list:
                for match in round:
                    pass
