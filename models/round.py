from random import Random
# from match import Match


class Round:
    def __init__(self, round_number, list_players):
        self.list_players = list_players
        self.round_number = round_number

    def define_matches(self):
        self.sort_list()
        for player in self.list_players:
            print(f'Joueur : {player.name}, score : {player.score}')

    def sort_list(self):
        if self.round_number == 1:
            Random().shuffle(self.list_players)
        else:
            self.list_players = reversed(sorted(self.list_players, key=lambda player: player.score))
