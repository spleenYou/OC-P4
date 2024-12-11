import datetime
from random import Random
from models.player import Player
from models.round import Round


class Tournament:
    """Define and manage a tournament

    Args:
        name (str): tournament's name
        place (str): tournament's place
        description (str): tournament's description
        date_start (str): tournament's start date if not filled in, day's date
        date_end (str): tournament's end date if not filled in, it's empty
    """
    def __init__(self,
                 name,
                 place,
                 description,
                 date_start="{:%d-%m-%Y}".format(datetime.date.today()),
                 date_end=""):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.rounds_list = []
        self.round_number = 0
        self.players_list = []
        self.description = description

    def is_finished(self):
        """Returns wether the tournament is over or not
        """
        if self.round_number < self.number_of_rounds():
            return False
        return True

    def count_round_number(self):
        """Count the number of round completed

        Returns
        """
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
        players_list = []
        if self.round_number == 0:
            Random().shuffle(self.players_list)
            players_list = self.players_list
        else:
            for player in self.players_list:
                players_list.append(player)
            number_matches = int(len(players_list) / 2)
            matches_possible = True
            while not matches_possible:
                for i in range(number_matches):
                    if not self.have_already_met(players_list[2 * i], players_list[2 * i + 1]):
                        player_to_move = players_list[2 * i + 1]
                        players_list.remove(player_to_move)
                        players_list.append(player_to_move)

        self.players_list = players_list

    def have_already_met(self, player_one, player_two):
        for round in self.rounds_list:
            for match in round.matches_list:
                if ((player_one == match.white_player["player"] or player_one == match.black_player["player"])
                   and (player_two == match.white_player["player"] or player_two == match.black_player["player"])):
                    return True
        return False

    def sort_list_by_score(self):
        self.players_list = sorted(self.players_list, key=lambda player: player.score, reverse=True)

    def next_round(self):
        self.round_number = self.round_number + 1

    def make_matches(self):
        self.rounds_list[self.round_number].make_matches(self.players_list)
        return None

    def end_of_tournament(self):
        self.date_end = "{:%d-%m-%Y}".format(datetime.date.today())

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
