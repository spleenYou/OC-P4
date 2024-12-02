import datetime
from random import Random
from models.player import Player
from models.round import Round


class Tournament:
    def __init__(self,
                 name,
                 place,
                 description,
                 id,
                 date_start="{:%d-%m-%Y}".format(datetime.date.today()),
                 date_stop='',
                 number_of_rounds=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_stop = date_stop
        self.rounds_list = []
        self.round_number = self.count_round_number()
        self.players_list = []
        self.description = description
        self.id = id

    def is_finished(self):
        for round in self.rounds_list:
            if not round.is_finished():
                return False
        return True

    def round_in_progress(self):
        for round in self.rounds_list:
            if not round.all_matches_finished():
                return round
        return None

    def matches_in_progress(self):
        return self.rounds_list[self.round_number - 1]

    def count_round_number(self):
        round_number = 0
        for round in self.rounds_list:
            if isinstance(round, Round):
                if not round.is_finished():
                    return round_number
                round_number = round_number + 1
        return round_number

    def add_player(self, new_player):
        self.players_list.append(new_player)

    def add_round(self, round=None):
        if round is None:
            round = Round()
        self.rounds_list.append(round)
        return None

    def has_all_players(self):
        for player in self.players_list:
            if not isinstance(player, Player):
                return False
        return True

    def __str__(self):
        for player in self.players_list:
            print(player)
        print(f'Nom : {self.name}\n'
              f'Endroit : {self.place}\n'
              f'Numero du tour : {self.round_number}\n'
              f'Date de début : {self.date_start}\n'
              f'Description : {self.description}\n'
              f'Nombre de tours : {self.number_of_rounds}')
        return ""

    def number_of_rounds(self):
        return len(self.rounds_list)

# a refaire
    def sort_list(self):
        if self.round_number == 1:
            Random().shuffle(self.players_list)
        else:
            self.players_list = sorted(self.players_list, key=lambda player: player.score, reverse=True)
            self.check_previous_meeting()
