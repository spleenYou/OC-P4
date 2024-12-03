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
        self.round_number = 0
        self.players_list = []
        self.description = description
        self.id = id
        self.round = Round()

    def is_finished(self):
        for round in self.rounds_list:
            if not round.is_finished():
                return False
        return True

    def count_round_number(self):
        for round in self.rounds_list:
            if not round.is_finished():
                return None
            self.round_number = self.round_number + 1

    def add_player(self, new_player):
        if len(self.players_list) and new_player != []:
            for i in range(len(self.players_list)):
                if self.players_list[i] == []:
                    self.players_list[i] = new_player
                    return None
            self.players_list.append(new_player)
        else:
            self.players_list.append(new_player)
        return None

    def add_round(self):
        round = Round()
        self.rounds_list.append(round)
        return round

    def has_all_players(self):
        for player in self.players_list:
            if not isinstance(player, Player):
                return False
        return True

    def number_of_rounds(self):
        return len(self.rounds_list)

    def sort_list(self):
        if self.round_number == 0:
            Random().shuffle(self.players_list)
            self.players_list_sort = self.players_list
        else:
            new_list_sort = []
            list_players = self.players_list_sort
            while len(list_players):
                i = 1
                if self.already_meet(list_players[0], list_players[i]):
                    i = i + 1
                else:
                    new_list_sort.append(list_players[0])
                    new_list_sort.append(list_players[i])
                    list_players.remove(list_players[i])
                    list_players.remove(list_players[0])
            self.players_list_sort = new_list_sort

    def already_meet(self, player_one, player_two):
        for round in self.rounds_list:
            for match in round.matches_list:
                if (any(player_one in player for player in match.score_table)
                   and any(player_two in player for player in match.score_table)):
                    return True
        return False

    def sort_list_by_score(self):
        self.players_list_sort = sorted(self.players_list, key=lambda player: player.score, reverse=True)

    def next_round(self):
        self.round_number = self.round_number + 1

    def make_matches(self):
        self.rounds_list[self.round_number].make_matches(self.players_list_sort)
        return None

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
