import datetime
from models.player import Player
from models.round import Round


class Tournament:
    def __init__(self,
                 name,
                 place,
                 rounds_list,
                 players_list,
                 description,
                 id,
                 date_start="{:%d-%m-%Y}".format(datetime.date.today()),
                 date_stop='',
                 number_of_rounds=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_stop = date_stop
        self.rounds_list = rounds_list
        self.round_number = self.count_round_number()
        self.players_list = players_list
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.id = id
        self.round = Round()

    def is_finished(self):
        if self.round_number < self.number_of_rounds:
            return False
        if self.rounds_list[-1].all_matches_finished():
            return True
        return False

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
            if self.round.is_finished():
                round_number = round_number + 1
            else:
                return round_number
        return round_number

    def add_player(self, new_player):
        for i in range(len(self.players_list)):
            if self.players_list[i] == []:
                self.players_list[i] = new_player
                break

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
