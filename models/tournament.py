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

    def __init__(
        self,
        name,
        place,
        description,
        date_start="{:%d-%m-%Y}".format(datetime.date.today()),
        date_end="",
    ):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.rounds_list = []
        self.round_number = 0
        self.players_list = []
        self.description = description

    def is_finished(self):
        """Returns wether the tournament is over or not"""
        if self.round_number < self.number_of_rounds():
            return False
        return True

    def count_round_number(self):
        "Count the number of round completed"
        for round in self.rounds_list:
            if round.is_finished():
                self.round_number = self.round_number + 1

    def add_player(self, new_player):
        """Add player in players_list

        Args:
            new_player (object): New player to be added to the list, can be None for list creation
        """
        if isinstance(new_player, Player):
            for i in range(len(self.players_list)):
                if self.players_list[i] is None:
                    self.players_list[i] = new_player
                    break
        else:
            self.players_list.append(new_player)

    def add_round(self):
        """Add a new round to the tournament

        Returns:
            round (object): Object of the new round
        """
        round = Round()
        self.rounds_list.append(round)
        return round

    def has_all_players(self):
        "Returns if tournament has at least one player in the list of players"
        for player in self.players_list:
            if not isinstance(player, Player):
                return False
        return True

    def number_of_rounds(self):
        "Returns the length of the list of rounds"
        return len(self.rounds_list)

    def sort_list(self):
        """If it's the first round, shuffle the list of players.
        For the next rounds, sort the list of players to make sure the players have never met each other
        """
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
                    if not self.have_already_met(
                        players_list[2 * i], players_list[2 * i + 1]
                    ):
                        player_to_move = players_list[2 * i + 1]
                        players_list.remove(player_to_move)
                        players_list.append(player_to_move)

        self.players_list = players_list

    def have_already_met(self, player_one, player_two):
        """Returns if two players already met each other

        Args:
            player_one (object): A player
            player_two (object): A player
        """
        for round in self.rounds_list:
            for match in round.matches_list:
                if (
                    player_one == match.white_player["player"]
                    or player_one == match.black_player["player"]
                ) and (
                    player_two == match.white_player["player"]
                    or player_two == match.black_player["player"]
                ):
                    return True
        return False

    def sort_list_by_score(self):
        "Sort the list of players by score (high in first)"
        self.players_list = sorted(
            self.players_list, key=lambda player: player.score, reverse=True
        )

    def next_round(self):
        "Increases by one the round number"
        self.round_number = self.round_number + 1

    def make_matches(self):
        "Call the fonction 'make_matches' for the round in progress"
        self.rounds_list[self.round_number].make_matches(self.players_list)

    def end_of_tournament(self):
        "Set the end date to today"
        self.date_end = "{:%d-%m-%Y}".format(datetime.date.today())
